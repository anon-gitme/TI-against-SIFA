from sbox_keccak_mitig import sbox_keccak_mitigated,\
                              sbox_keccak_mitigated_register_stk0,\
                              sbox_keccak_mitigated_register_stk1,\
                              sbox_keccak_mitigated_register_flip,\
                              sbox_keccak_mitigated_register_rand,\
                              sbox_keccak_mitigated_cfunc_stk0,\
                              sbox_keccak_mitigated_cfunc_stk1,\
                              sbox_keccak_mitigated_cfunc_flip,\
                              sbox_keccak_mitigated_cfunc_rand
from sbox_keccak_vul import sbox_keccak_reference,\
                            sbox_keccak_vulnerable
from sbox_led_vul import sbox_led_vulnerable
from sbox_led_mitig import sbox_led_mitigated,\
                           sbox_led_mitigated_register_stk0,\
                           sbox_led_mitigated_register_stk1,\
                           sbox_led_mitigated_register_flip,\
                           sbox_led_mitigated_register_rand,\
                           sbox_led_mitigated_component_function_stk0,\
                           sbox_led_mitigated_component_function_stk1,\
                           sbox_led_mitigated_component_function_flip,\
                           sbox_led_mitigated_component_function_rand
from outils import bit_shares_to_word
from tqdm import tqdm
from collections import Counter
from scipy.special import kl_div
import matplotlib.pyplot as plt
import os

def analyze_sbox(config):
    # Keccak: vulnerable
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_keccak_with_faults_in_component_function(sbox_keccak_reference, 
                                                                            sbox_keccak_vulnerable)
    print("\n >>>>>>>>>> Keccak -  SFA - component function - stk0 (exploitable) <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 32, "figs/keccak_sfa_vul.png")
    print("\n >>>>>>>>>> Keccak - SIFA - component function - stk0 (exploitable) <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 32, "figs/keccak_sifa_vul.png")

    ###############################################
    ######### KECCAK: FAULTS IN REGISTER ##########
    ###############################################

    # Keccak: unexploitable, stuck-at-0 faults in register
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_keccak_with_faults_in_register(sbox_keccak_mitigated, 
                                                                  sbox_keccak_mitigated_register_stk0)
    print("\n >>>>>>>>>> Keccak -  SFA - register - stk0 <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 32, "figs/keccak_sfa_faults_register_stk0.png")
    print("\n >>>>>>>>>> Keccak - SIFA - register - stk0 <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 32, "figs/keccak_sifa_faults_register_stk0.png")

    # Keccak: unexploitable, stuck-at-1 faults in register
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_keccak_with_faults_in_register(sbox_keccak_mitigated, 
                                                                  sbox_keccak_mitigated_register_stk1)
    print("\n >>>>>>>>>> Keccak -  SFA - register - stk1 <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 32, "figs/keccak_sfa_faults_register_stk1.png")
    print("\n >>>>>>>>>> Keccak - SIFA - register - stk1 <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 32, "figs/keccak_sifa_faults_register_stk1.png")

    # Keccak: unexploitable, flipping faults in register
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_keccak_with_faults_in_register(sbox_keccak_mitigated, 
                                                                  sbox_keccak_mitigated_register_flip)
    print("\n >>>>>>>>>> Keccak -  SFA - register - flip <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 32, "figs/keccak_sfa_faults_register_flip.png")
    print("\n >>>>>>>>>> Keccak - SIFA - register - flip <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 32, "figs/keccak_sifa_faults_register_flip.png")

    # Keccak: unexploitable, random faults in register
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_keccak_with_faults_in_register(sbox_keccak_mitigated, 
                                                                  sbox_keccak_mitigated_register_rand)
    print("\n >>>>>>>>>> Keccak -  SFA - register - rand <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 32, "figs/keccak_sfa_faults_register_rand.png")
    print("\n >>>>>>>>>> Keccak - SIFA - register - rand <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 32, "figs/keccak_sifa_faults_register_rand.png")

    ##########################################################
    ########## KECCAK: FAULTS IN COMPONENT FUNCTION ##########
    ##########################################################

    # Keccak: unexploitable, stuck-at-0 faults in a component function
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_keccak_with_faults_in_component_function(sbox_keccak_mitigated, 
                                                                            sbox_keccak_mitigated_cfunc_stk0)
    print("\n >>>>>>>>>> Keccak -  SFA - component function - stk0 <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 32, "figs/keccak_sfa_faults_cfunc_stk0.png")
    print("\n >>>>>>>>>> Keccak - SIFA - component function - stk0 <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 32, "figs/keccak_sifa_faults_cfunc_stk0.png")

    # Keccak: unexploitable, stuck-at 1 faults in a component function
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_keccak_with_faults_in_component_function(sbox_keccak_mitigated, 
                                                                            sbox_keccak_mitigated_cfunc_stk1)
    print("\n >>>>>>>>>> Keccak -  SFA - component function - stk1 <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 32, "figs/keccak_sfa_faults_cfunc_stk1.png")
    print("\n >>>>>>>>>> Keccak - SIFA - component function - stk1 <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 32, "figs/keccak_sifa_faults_cfunc_stk1.png")

    # Keccak: unexploitable, flipping faults in a component function
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_keccak_with_faults_in_component_function(sbox_keccak_mitigated, 
                                                                            sbox_keccak_mitigated_cfunc_flip)
    print("\n >>>>>>>>>> Keccak -  SFA - component function - flip <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 32, "figs/keccak_sfa_faults_cfunc_flip.png")
    print("\n >>>>>>>>>> Keccak - SIFA - component function - flip <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 32, "figs/keccak_sifa_faults_cfunc_flip.png")

    # Keccak: unexploitable, random faults in a component function
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_keccak_with_faults_in_component_function(sbox_keccak_mitigated, 
                                                                            sbox_keccak_mitigated_cfunc_rand)
    print("\n >>>>>>>>>> Keccak -  SFA - component function - rand <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 32, "figs/keccak_sfa_faults_cfunc_rand.png")
    print("\n >>>>>>>>>> Keccak - SIFA - component function - rand <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 32, "figs/keccak_sifa_faults_cfunc_rand.png")


    #############################################
    ########## LED: FAULTS IN REGISTER ##########
    #############################################

    # LED: unexploitable, stuck-at-0 faults in register
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_led_with_faults_in_register(sbox_led_mitigated, 
                                                               sbox_led_mitigated_register_stk0)
    print("\n >>>>>>>>>> LED -  SFA - register - stk0 <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 16, "figs/led_sfa_faults_register_stk0.png")
    print("\n >>>>>>>>>> LED - SIFA - register - stk0 <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 16, "figs/led_sifa_faults_register_stk0.png")
    
    # LED: unexploitable, stuck-at-1 faults in register
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_led_with_faults_in_register(sbox_led_mitigated, 
                                                               sbox_led_mitigated_register_stk1)
    print("\n >>>>>>>>>> LED -  SFA - register - stk1 <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 16, "figs/led_sfa_faults_register_stk1.png")
    print("\n >>>>>>>>>> LED - SIFA - register - stk1 <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 16, "figs/led_sifa_faults_register_stk1.png")
    
    # LED: unexploitable, flip faults in register
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_led_with_faults_in_register(sbox_led_mitigated, 
                                                               sbox_led_mitigated_register_flip)
    print("\n >>>>>>>>>> LED -  SFA - register - flip <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 16, "figs/led_sfa_faults_register_flip.png")
    print("\n >>>>>>>>>> LED - SIFA - register - flip <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 16, "figs/led_sifa_faults_register_flip.png")
    
    # LED: unexploitable, random faults in register
    # Note: too little samples to see the uniform distribution for random faults!
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_led_with_faults_in_register(sbox_led_mitigated, 
                                                               sbox_led_mitigated_register_rand)
    print("\n >>>>>>>>>> LED -  SFA - register - rand <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 16, "figs/led_sfa_faults_register_rand.png")
    print("\n >>>>>>>>>> LED - SIFA - register - rand <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 16, "figs/led_sifa_faults_register_rand.png")
    
    #######################################################
    ########## LED: FAULTS IN COMPONENT FUNCTION ##########
    #######################################################

    # LED: unexploitable, stuck-at-0 faults in a component function
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_led_with_faults_in_component_function(sbox_led_mitigated, 
                                                                         sbox_led_mitigated_component_function_stk0)
    print("\n >>>>>>>>>> LED -  SFA - component function - stk0 <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 16, "figs/led_sfa_faults_cfunc_stk0.png")
    print("\n >>>>>>>>>> LED - SIFA - component function - stk0 <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 16, "figs/led_sifa_faults_cfunc_stk0.png")
    

    # LED: unexploitable, stuck-at 1 faults in a component function
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_led_with_faults_in_component_function(sbox_led_mitigated, 
                                                                         sbox_led_mitigated_component_function_stk1)
    print("\n >>>>>>>>>> LED -  SFA - component function - stk1 <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 16, "figs/led_sfa_faults_cfunc_stk1.png")
    print("\n >>>>>>>>>> LED - SIFA - component function - stk1 <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 16, "figs/led_sifa_faults_cfunc_stk1.png")
    
    # LED: unexploitable, flipping faults in a component function
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_led_with_faults_in_component_function(sbox_led_mitigated, 
                                                                         sbox_led_mitigated_component_function_flip)
    print("\n >>>>>>>>>> LED -  SFA - component function - flip <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 16, "figs/led_sfa_faults_cfunc_flip.png")
    print("\n >>>>>>>>>> LED - SIFA - component function - flip <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 16, "figs/led_sifa_faults_cfunc_flip.png")
    
    # # LED: unexploitable, random faults in a component function
    sfa_inps, sfa_outs,\
    sifa_inps, sifa_outs = analyze_led_with_faults_in_component_function(sbox_led_mitigated, 
                                                                         sbox_led_mitigated_component_function_rand)
    print("\n >>>>>>>>>> LED -  SFA - component function - rand <<<<<<<<<<\n")
    draw_inout_distribution(config, sfa_inps, sfa_outs, 16, "figs/led_sfa_faults_cfunc_rand.png")
    print("\n >>>>>>>>>> LED - SIFA - component function - rand <<<<<<<<<<\n")
    draw_inout_distribution(config, sifa_inps, sifa_outs, 16, "figs/led_sifa_faults_cfunc_rand.png")
    


def analyze_led_with_faults_in_component_function(func_correct, func_faulty):
    """
    """
    sifa_inps = []
    sifa_outs = []

    sfa_inps = []
    sfa_outs = []

    for n in tqdm(range(1<<12)):
        x11 =  n & 1
        x12 = (n >> 1) & 1
        x13 = (n >> 2) & 1
        x21 = (n >> 3) & 1
        x22 = (n >> 4) & 1
        x23 = (n >> 5) & 1
        x31 = (n >> 6) & 1
        x32 = (n >> 7) & 1
        x33 = (n >> 8) & 1
        x41 = (n >> 9) & 1
        x42 = (n >> 10) & 1
        x43 = (n >> 11) & 1

        a11, a12, a13,\
        a21, a22, a23,\
        a31, a32, a33,\
        a41, a42, a43 = func_correct(x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43)

        fa11, fa12, fa13,\
        fa21, fa22, fa23,\
        fa31, fa32, fa33,\
        fa41, fa42, fa43 = func_faulty(x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43)

        x = bit_shares_to_word([x11, x12, x13,
                                x21, x22, x23,
                                x31, x32, x33,
                                x41, x42, x43], 4, 3)
        a = bit_shares_to_word([a11, a12, a13,
                                a21, a22, a23,
                                a31, a32, a33,
                                a41, a42, a43], 4, 3)
        fa = bit_shares_to_word([fa11, fa12, fa13,
                                 fa21, fa22, fa23,
                                 fa31, fa32, fa33,
                                 fa41, fa42, fa43], 4, 3)
        
        sfa_inps.append(x)
        sfa_outs.append(fa)

        if a == fa:
            sifa_inps.append(x)
            sifa_outs.append(fa)
    
    return sfa_inps, sfa_outs, sifa_inps, sifa_outs

def analyze_led_with_faults_in_register(func_correct, func_faulty):
    """
    """
    sifa_inps = []
    sifa_outs = []

    sfa_inps = []
    sfa_outs = []

    for n in tqdm(range(1<<12)):
        x11 =  n & 1
        x12 = (n >> 1) & 1
        x13 = (n >> 2) & 1
        x21 = (n >> 3) & 1
        x22 = (n >> 4) & 1
        x23 = (n >> 5) & 1
        x31 = (n >> 6) & 1
        x32 = (n >> 7) & 1
        x33 = (n >> 8) & 1
        x41 = (n >> 9) & 1
        x42 = (n >> 10) & 1
        x43 = (n >> 11) & 1

        a11, a12, a13,\
        a21, a22, a23,\
        a31, a32, a33,\
        a41, a42, a43 = func_correct(x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43)

        fx_sh, fa_sh = func_faulty(x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43)

        x = bit_shares_to_word([x11, x12, x13,
                                x21, x22, x23,
                                x31, x32, x33,
                                x41, x42, x43], 4, 3)
        fx = bit_shares_to_word(fx_sh, 4, 3)
        a = bit_shares_to_word([a11, a12, a13,
                                a21, a22, a23,
                                a31, a32, a33,
                                a41, a42, a43], 4, 3)
        fa = bit_shares_to_word(fa_sh, 4, 3)
        
        sfa_inps.append(fx)
        sfa_outs.append(fa)

        if a == fa:
            sifa_inps.append(fx)
            sifa_outs.append(fa)
    
    return sfa_inps, sfa_outs, sifa_inps, sifa_outs

def analyze_keccak_with_faults_in_component_function(func_correct, func_faulty):
    """
    """
    
    sifa_inps = []
    sifa_outs = []

    sfa_inps = []
    sfa_outs = []

    for n in tqdm(range(1<<20)):
        x00 =  n & 1
        x01 = (n >> 1) & 1
        x02 = (n >> 2) & 1
        x03 = (n >> 3) & 1
        x10 = (n >> 4) & 1
        x11 = (n >> 5) & 1
        x12 = (n >> 6) & 1
        x13 = (n >> 7) & 1
        x20 = (n >> 8) & 1
        x21 = (n >> 9) & 1
        x22 = (n >> 10) & 1
        x23 = (n >> 11) & 1
        x30 = (n >> 12) & 1
        x31 = (n >> 13) & 1
        x32 = (n >> 14) & 1
        x33 = (n >> 15) & 1
        x40 = (n >> 16) & 1
        x41 = (n >> 17) & 1
        x42 = (n >> 18) & 1
        x43 = (n >> 19) & 1

        a00, a01, a02, a03,\
        a10, a11, a12, a13,\
        a20, a21, a22, a23,\
        a30, a31, a32, a33,\
        a40, a41, a42, a43 = func_correct(x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43)

        fa00, fa01, fa02, fa03,\
        fa10, fa11, fa12, fa13,\
        fa20, fa21, fa22, fa23,\
        fa30, fa31, fa32, fa33,\
        fa40, fa41, fa42, fa43 = func_faulty(x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43)

        x = bit_shares_to_word([x00, x01, x02, x03, 
                                x10, x11, x12, x13, 
                                x20, x21, x22, x23, 
                                x30, x31, x32, x33, 
                                x40, x41, x42, x43],
                                nb=5, ns=4)
        a = bit_shares_to_word([a00, a01, a02, a03, 
                                a10, a11, a12, a13, 
                                a20, a21, a22, a23, 
                                a30, a31, a32, a33, 
                                a40, a41, a42, a43],
                                nb=5, ns=4)
        fa = bit_shares_to_word([fa00, fa01, fa02, fa03, 
                                fa10, fa11, fa12, fa13, 
                                fa20, fa21, fa22, fa23, 
                                fa30, fa31, fa32, fa33, 
                                fa40, fa41, fa42, fa43],
                                nb=5, ns=4)

        # SFA
        sfa_inps.append(x)
        sfa_outs.append(fa)

        # SIFA
        if a == fa:
            sifa_inps.append(x)
            sifa_outs.append(a)

    return sfa_inps, sfa_outs, sifa_inps, sifa_outs

def analyze_keccak_with_faults_in_register(func_correct, func_faulty):
    """
    """
    
    sifa_inps = []
    sifa_outs = []

    sfa_inps = []
    sfa_outs = []

    for n in tqdm(range(1<<20)):
        x00 =  n & 1
        x01 = (n >> 1) & 1
        x02 = (n >> 2) & 1
        x03 = (n >> 3) & 1
        x10 = (n >> 4) & 1
        x11 = (n >> 5) & 1
        x12 = (n >> 6) & 1
        x13 = (n >> 7) & 1
        x20 = (n >> 8) & 1
        x21 = (n >> 9) & 1
        x22 = (n >> 10) & 1
        x23 = (n >> 11) & 1
        x30 = (n >> 12) & 1
        x31 = (n >> 13) & 1
        x32 = (n >> 14) & 1
        x33 = (n >> 15) & 1
        x40 = (n >> 16) & 1
        x41 = (n >> 17) & 1
        x42 = (n >> 18) & 1
        x43 = (n >> 19) & 1

        a00, a01, a02, a03,\
        a10, a11, a12, a13,\
        a20, a21, a22, a23,\
        a30, a31, a32, a33,\
        a40, a41, a42, a43 = func_correct(x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43)

        fx_sh, fa_sh = func_faulty(x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43)

        x = bit_shares_to_word([x00, x01, x02, x03, 
                                x10, x11, x12, x13, 
                                x20, x21, x22, x23, 
                                x30, x31, x32, x33, 
                                x40, x41, x42, x43],
                                nb=5, ns=4)
        fx = bit_shares_to_word(fx_sh, nb=5, ns=4)
        a = bit_shares_to_word([a00, a01, a02, a03, 
                                a10, a11, a12, a13, 
                                a20, a21, a22, a23, 
                                a30, a31, a32, a33, 
                                a40, a41, a42, a43],
                                nb=5, ns=4)
        fa = bit_shares_to_word(fa_sh, nb=5, ns=4)

        # SFA
        sfa_inps.append(fx)
        sfa_outs.append(fa)

        # SIFA
        if a == fa:
            sifa_inps.append(fx)
            sifa_outs.append(fa)

    return sfa_inps, sfa_outs, sifa_inps, sifa_outs


def draw_inout_distribution(config, inps, outs, nbins, outfile):
    if not os.path.exists(config.figure_folder):
        os.makedirs(config.figure_folder)

    fig, axs = plt.subplots(2)
    fig.set_figwidth(10)
    axs[0].hist(inps, bins=nbins, edgecolor="white")
    axs[1].hist(outs, bins=nbins, edgecolor="white")
    plt.savefig(outfile)
    plt.close()

    M = len(inps)
    counter_inp = Counter(inps)
    counter_out = Counter(outs)

    cnt_inp = [c for _,c in sorted(counter_inp.items())]
    cnt_out = [c for _,c in sorted(counter_out.items())]

    if cnt_inp == [] and cnt_out == []:
        cnt_inp = [0] * nbins
        cnt_out = [0] * nbins

    if M == 0:
        proba_inp = [0 for _ in cnt_inp]
        proba_out = [0 for _ in cnt_out]
    else:
        proba_inp = [c/M for c in cnt_inp]
        proba_out = [c/M for c in cnt_out]

    KL_inp = sum(list(kl_div(proba_inp, [1/nbins] * nbins)))
    KL_out = sum(list(kl_div(proba_out, [1/nbins] * nbins)))

    print(f"Number of samples: {M}")
    print("  IN : ", end="")
    for p in proba_inp:
        print(f"{p*100:.3f} ", end="")
    print()

    print("  OUT: ", end="")
    for p in proba_out:
        print(f"{p*100:.3f} ", end="")
    print()

    print(f"IN : KL: {KL_inp}")
    print(f"OUT: KL: {KL_out}")
    
    return proba_inp, proba_out