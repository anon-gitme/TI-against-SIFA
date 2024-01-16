from faulting import setup_cw, close_cw, do_faulting

def collect(config):
    '''

    '''
    scope, gc, target = setup_cw(config)

    fm = open(config.path_to_plaintext_file, "r")
    fc = open(config.path_to_ciphertext_file, "r")
    fo = open(config.path_to_cw_ciphertext_file, "w+")

    key = bytes.fromhex(config.key)

    count = 0
    while True:
        m = bytes.fromhex(fm.readline().strip())
        c = bytes.fromhex(fc.readline().strip())

        if not m or not c:
            break

        count += 1
        print(f"================ {count}/{config.M} ================")

        indata = bytearray(m + key)
        cmpdata = bytearray(c)

        outdata = do_faulting(scope, gc, target, indata, cmpdata, config.N)
        for cw_c in outdata:
            cw_c = bytes(cw_c)
            fo.write(cw_c.hex())
            fo.write("\n")

    fm.close()
    fc.close()
    fo.close()
    close_cw(scope, target)