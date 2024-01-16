from LED import RawLED,\
                inv_shift_rows,\
                inv_mix_columns_serial,\
                inv_add_round_key,\
                inv_sub_cells,\
                inv_add_constants
from collections import Counter
from outils import draw_distribution
from random import randint

def analyze(config):
    correct_last_step_key = [v for x in bytes.fromhex(config.correct_last_step_key) 
                               for  v in ((x >> 4) & 0xF, x & 0xF)]
    wrong_last_step_key = [randint(0,15) for _ in range(16)]
    assert wrong_last_step_key != correct_last_step_key

    analyze_with_ciphertexts(config, 
                           config.path_to_ciphertext_file,
                           config.path_to_cw_ciphertext_file,
                           correct_last_step_key,
                           wrong_last_step_key,
                           config.outfile_prefix)




def analyze_with_ciphertexts(config, 
                             path_to_ref_ciphertext_file, 
                             path_to_cw_ciphertext_file, 
                             correct_key_guess,
                             wrong_key_guess,
                             outfile_prefix):
    f = open(path_to_cw_ciphertext_file, "r")
    cw_cpts = f.readlines()
    f.close()

    f = open(path_to_ref_ciphertext_file, "r")
    ref_cpts = f.readlines()
    f.close()

    cw_cpts = [[v for x in bytes.fromhex(line) for v in ((x >> 4) & 0xF, x & 0xF)] for line in cw_cpts]    
    ref_cpts= [[v for x in bytes.fromhex(line) for v in ((x >> 4) & 0xF, x & 0xF)] for line in ref_cpts]

    print("\n@@@@@@@@@@ Correct Key @@@@@@@@@@\n")
    analyze_with_key_guess(config, cw_cpts, ref_cpts, correct_key_guess, f"{outfile_prefix}_correctkey")
    print("\n@@@@@@@@@@ Wrong Key @@@@@@@@@@\n")
    analyze_with_key_guess(config, cw_cpts, ref_cpts, wrong_key_guess, f"{outfile_prefix}_wrongkey")


def analyze_with_key_guess(config, cw_cpts, ref_cpts, key_guess, outfile_prefix):
    M = len(ref_cpts)
    L = len(cw_cpts)
    N = config.N
    assert L == N * M

    sfa_nibs = [compute_backward(cpt, key_guess) for cpt in cw_cpts]
    
    sifa_nibs = []
    for i in range(M):
        ref_c = ref_cpts[i]
        for j in range(N):
            c = cw_cpts[i*N+j]
            if c == ref_c:
                sifa_nibs.append(sfa_nibs[i*N+j])

    print("\n>>>>>>>>>> SIFA <<<<<<<<<<\n")
    draw_distribution(config, sifa_nibs, 16, f"figures/{outfile_prefix}_sifa-distr.png", divisor=N)
    print("\n>>>>>>>>>> SFA <<<<<<<<<<\n")
    draw_distribution(config, sfa_nibs , 16, f"figures/{outfile_prefix}_sfa-distr.png", divisor=N)



def compute_backward(ciphertext, key_guess):
    state = inv_add_round_key(ciphertext, key_guess)
    state = inv_mix_columns_serial(state)
    state = inv_shift_rows(state)
    state = inv_sub_cells(state)
    state = inv_add_constants(state)
    state = inv_mix_columns_serial(state)
    return state[0]