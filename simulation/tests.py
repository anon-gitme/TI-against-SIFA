from outils import word_to_bit_shares, bit_shares_to_word
from sbox_led_mitig import sbox_led_mitigated
from sbox_keccak_vul import sbox_keccak_reference
from sbox_keccak_mitig import sbox_keccak_mitigated
from random import randint

def test_word_and_bit_shares_convertion():
    # 4-bit word, 3 shares
    v_ref = randint(0, 15)
    bit_shares = word_to_bit_shares(v_ref, 4, 3)
    v = bit_shares_to_word(bit_shares, 4, 3)
    assert v == v_ref

    # 5-bit word, 4 shares
    v_ref = randint(0, 31)
    bit_shares = word_to_bit_shares(v_ref, 5, 4)
    v = bit_shares_to_word(bit_shares, 5, 4)
    assert v == v_ref
    print("Test 1: word and bit shares convertion...OK")

def test_sbox_led_reference():
    SBOX = [0xC, 0x5, 0x6, 0xB, 0x9, 0x0, 0xA, 0xD, 0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2]
    x = randint(0, 15)
    y = bit_shares_to_word(sbox_led_mitigated(*word_to_bit_shares(x, 4, 3)), 4, 3)
    assert y == SBOX[x]
    print("Test 2: LED S-box...OK")

def test_sbox_keccak_reference():
    SBOX = [0, 9, 18, 11, 5, 12, 22, 15, 10, 3, 24, 1, 13, 4, 30, 7, 20, 21, 6, 23, 17, 16, 2, 19, 26, 27, 8, 25, 29, 28, 14, 31]
    x = randint(0, 31)
    y = bit_shares_to_word(sbox_keccak_reference(*word_to_bit_shares(x, 5, 4)), 5, 4)
    assert y == SBOX[x]

    y = bit_shares_to_word(sbox_keccak_mitigated(*word_to_bit_shares(x, 5, 4)), 5, 4)
    assert y == SBOX[x]
    print("Test 3: Keccak S-box...OK")

def test_all():
    test_word_and_bit_shares_convertion()
    test_sbox_led_reference()
    test_sbox_keccak_reference()