from tqdm import tqdm
from LED import RawLED
import os


def prepare(config):
    '''
    :param config:
    '''
    print("Sampling a set of plaintexts and encrypting...")

    k4 = [v for x in bytes.fromhex(config.key) for  v in ((x >> 4) & 0xF, x & 0xF)]
    cipher = RawLED(k4)

    fm = open(config.path_to_plaintext_file, "w+")
    fc = open(config.path_to_ciphertext_file, "w+")

    for _ in tqdm(range(config.M)):
        m = os.urandom(8)
        m4 = [v for x in m for v in ((x >> 4) & 0xF, x & 0xF)]
        c4 = cipher.encrypt(m4)
        c = bytes([(c4[i*2] << 4) | c4[i*2+1] for i in range(8)])

        fm.write(m.hex())
        fc.write(c.hex())
        fm.write("\n")
        fc.write("\n")
        
    fm.close()