from analyzer import analyze_led_with_faults_in_register
from sbox_led_mitig import sbox_led_mitigated, sbox_led_mitigated_register_rand
from collections import Counter
from scipy.special import kl_div
import matplotlib.pyplot as plt

def rep_analyze(config):
    ####################################################################################
    ######### LED: FAULTS IN REGISTER (REPEAT SEVERAL TIMES FOR RANDOM FAULT) ##########
    ####################################################################################

    total_sifa_inps = []
    total_sifa_outs = []
    DKL_inps = []
    DKL_outs = []

    for i in range(config.rep):
        print(f"\n >>>>>>>>>> LED - SIFA - register - rand (repetition: {i}) <<<<<<<<<<\n")

        sfa_inps, sfa_outs,\
        sifa_inps, sifa_outs = analyze_led_with_faults_in_register(sbox_led_mitigated, 
                                                                    sbox_led_mitigated_register_rand)
        
        total_sifa_inps += sifa_inps
        total_sifa_outs += sifa_outs

        M = len(total_sifa_inps)
        counter_inp = Counter(total_sifa_inps)
        counter_out = Counter(total_sifa_outs)

        cnt_inp = [c for _,c in sorted(counter_inp.items())]
        cnt_out = [c for _,c in sorted(counter_out.items())]

        proba_inp = [c/M for c in cnt_inp]
        proba_out = [c/M for c in cnt_out]

        KL_inp = sum(list(kl_div(proba_inp, [1/16] * 16)))
        KL_out = sum(list(kl_div(proba_out, [1/16] * 16)))
        
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

        DKL_inps.append(KL_inp)
        DKL_outs.append(KL_out)

    plt.figure().set_figwidth(14)
    xs = [x+1 for x in range(config.rep)]
    yI = [v for v in DKL_inps]
    yO = [v+0.0005 for v in DKL_outs]
    plt.plot(xs, yI, '-o', color='red', label=r"Input")
    plt.plot(xs, yO, '-o', color='blue', label=r"Output")
    
    plt.legend(loc="best")
    plt.xlim(0.5, config.rep + 1)
    plt.ylim(0, 0.04)

    plt.xlabel(r"Number of repetitions")
    plt.ylabel(r"$D_{KL}$")

    plt.savefig("figs/led_sifa_faults_register_rand_repetition.png")
    plt.close() 

