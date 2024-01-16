from analyzer import analyze_sbox
from rep_analyzer import rep_analyze
from tests import test_all

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-test",
                        dest="is_test",
                        action="store_true",
                        help="Run test vectors",
                        default=False)
    parser.add_argument("-analyze",
                        dest="is_analyze",
                        action="store_true",
                        help="Analyze distribution of faulty S-box",
                        default=False)
    parser.add_argument("-rep-analyze",
                        dest="is_rep_analyze",
                        action="store_true",
                        help="Analyze distribution of with repetition",
                        default=False)
    parser.add_argument("-rep",
                        dest="rep",
                        help="Number of repetitions",
                        type=int,
                        default=20)
    parser.add_argument("-ff",
                        dest="figure_folder",
                        help="Folder to store figures",
                        type=str,
                        default="figs")
    
    config = parser.parse_args()

    if config.is_test:
        test_all()
    if config.is_analyze:
        analyze_sbox(config)
    if config.is_rep_analyze:
        rep_analyze(config)