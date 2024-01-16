from faulting import do_faulting
from preparator import prepare
from collector import collect
from analyzer import analyze
import argparse



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-prepare",
                        dest="is_preparation",
                        action="store_true",
                        help="Generate a set of plaintexts",
                        default=False)
    
    parser.add_argument("-collect",
                        dest="is_collection",
                        action="store_true",
                        help="Connect to CW and collect correct/faulty ciphertexts",
                        default=False)
    
    parser.add_argument("-analyze",
                        dest="is_analysis",
                        action="store_true",
                        help="Compute backward to verify the uniformity",
                        default=False)
    
    parser.add_argument("-vul",
                        dest="is_vulnerable",
                        action="store_true",
                        help="Compute backward to verify the uniformity",
                        default=False)

    parser.add_argument("-M",
                        dest="M",
                        help="Number of plaintexts",
                        type=int,
                        default=2688)

    parser.add_argument("-N",
                        dest="N",
                        help="Number of correct/faulty ciphertexts in glitching for each plaintext",
                        type=int,
                        default=50)
    
    parser.add_argument("-key",
                        dest="key",
                        help="Fixed key for experiment in hexadecimal",
                        type=str,
                        default="0123456789abcdef0123456789abcdef")

    parser.add_argument("-last-step-key",
                        dest="correct_last_step_key",
                        help="Correct last step key in hexadecimal",
                        type=str,
                        default="0123456789abcdef")

    parser.add_argument("-fm",
                        dest="path_to_plaintext_file",
                        help="Path to plaintext file",
                        type=str,
                        default="data/vu-stlr8192_m.txt")
    
    parser.add_argument("-fc",
                        dest="path_to_ciphertext_file",
                        help="Path to ciphertext file",
                        type=str,
                        default="data/vu-stlr8192_c.txt")
    
    parser.add_argument("-fo",
                        dest="path_to_cw_ciphertext_file",
                        help="Path to ciphertext file obtained from CW",
                        type=str,
                        default="data/vu-stlr8192_cw.txt")
    
    parser.add_argument("-prefix",
                        dest="outfile_prefix",
                        help="Prefix to differentiate filename",
                        type=str,
                        default="vu")
    

    config = parser.parse_args()

    if config.is_preparation:
        prepare(config)
    if config.is_collection:
        collect(config)
    if config.is_analysis:
        analyze(config)

    # print(config.key)

    # indataset = [bytearray([0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef,
    #                             0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef,
    #                             0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef])]
    # outdataset = [bytearray([0xd6, 0xb8, 0x24, 0x58, 0x7f, 0x01, 0x4f, 0xc2])]
if __name__ == "__main__":
    main()