import chipwhisperer as cw
import time

def reboot_flush(scope, target):            
    scope.io.nrst = False
    time.sleep(0.05)
    scope.io.nrst = "high_z"
    time.sleep(0.05)
    #Flush garbage too
    target.flush()

def setup_cw(config):
    PLATFORM = "CWLITEARM"
    scope = cw.scope()

    # SS_VER == "SS_VER_2_1":
    target_type = cw.targets.SimpleSerial2
    target = cw.target(scope, target_type)
    print("INFO: Found ChipWhisperer😍")

    # CWLITEARM
    prog = cw.programmers.STM32FProgrammer
    scope.default_setup()

    if config.is_vulnerable:
        fw_path = f"simpleserial-glitch-vu/simpleserial-glitch-{PLATFORM}.hex"
    else:
        fw_path = f"simpleserial-glitch/simpleserial-glitch-{PLATFORM}.hex"
    cw.program_target(scope, prog, fw_path)
    target.reset_comms()

    '''
    reboot_flush(scope, target)
    data = bytearray([0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef,
                      0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef,
                      0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef])
    target.simpleserial_write('p', data)
    val = target.simpleserial_read_witherrors('r', 8, glitch_timeout=10)
    print(val)
    '''

    gc = cw.GlitchController(groups=["success", "reset", "normal"], 
                             parameters=["width", "offset", "ext_offset"])
    gc.display_stats()

    scope.glitch.clk_src = "clkgen" 
    scope.glitch.output = "clock_xor"
    scope.glitch.trigger_src = "ext_single"
    scope.glitch.repeat = 5
    scope.io.hs2 = "glitch"
    # scope.cglitch_setup()


    if config.is_vulnerable:
        gc.set_range("width", 8, 10)
        gc.set_range("offset", 4, 5.8)
        gc.set_range("ext_offset", 485, 875)
        gc.set_global_step(0.2)
        gc.set_step("ext_offset", 5)
    else:
        gc.set_range("width", 8, 10)
        gc.set_range("offset", 4, 5.8)
        gc.set_range("ext_offset", 180, 210)
        gc.set_global_step(0.2)
        gc.set_step("ext_offset", 1)

    scope.glitch.repeat = 1
    reboot_flush(scope, target)
    scope.adc.timeout = 1

    return scope, gc, target

def close_cw(scope, target):
    scope.dis()
    target.dis()
    print("Done glitching :) Good bye!")


def do_faulting(scope, gc, target, indata, cmpdata, N):
    '''
    :param indata   :
    :param cmpdata  :
    :param N        :
    '''
    outdata = []

    # Counters for correct and faulty ciphertexts
    count_correct = 0
    count_faulty  = 0
    
    for glitch_setting in gc.glitch_values():
        scope.glitch.offset = glitch_setting[1]
        scope.glitch.width = glitch_setting[0]
        scope.glitch.ext_offset = glitch_setting[2]

        if scope.adc.state:
            print("[RESET] Trigger still high!")
            gc.add("reset")
            reboot_flush(scope, target)

        # Send plaintext and trigger glitch
        scope.arm()
        target.simpleserial_write('p', indata)
        ret = scope.capture()

        if ret:
            print("[RESET] Timeout, no trigger!")
            gc.add("reset")
            reboot_flush(scope, target)
        else:
            response = target.simpleserial_read_witherrors('r', 8, glitch_timeout=10, timeout=50)
            
            # Invalid response
            if response['valid'] is False:
                print("[RESET] Invalid response!")
                gc.add("reset")
                reboot_flush(scope, target)

            # Good response, including:
            #   - No fault: glitch does not work
            #   - Ineffective fault: computation is tampered, but does not affect the output
            #   - Effective fault: computation is tampered, and does affect the output
            else:
                print(f"[OK] {response['payload']} - ", end="")
                outdata.append(response['payload'])
                if response['payload'] == cmpdata:
                    count_correct += 1
                    gc.add("success")
                    print("Correct!", end="")
                else:
                    count_faulty += 1
                    gc.add("normal")
                    print("Faulty !", end="")
                    # print(f"\n W = {glitch_setting[0]} O = {glitch_setting[1]} E = {glitch_setting[2]}")
                print(f" (INFO: {count_correct} C, {count_faulty} F)")
                if count_correct + count_faulty == N:
                    break

    return outdata