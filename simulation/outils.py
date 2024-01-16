from random import randint

def word_to_bits(v, nb):
    """
    :param v : value of word
    :param nb: bitsize of word
    :return  : list of bits from LSB to MSB
    """
    bits = []
    for i in range(nb):
        b = (v >> i) & 1
        bits.append(b)
    return bits

def bits_to_word(bits, nb):
    """
    :param bits: list of bits from LSB to MSB
    :param nb  : bitsize
    :return    : word
    """
    v = 0
    for i in range(nb):
        b = bits[i]
        v |= (b << i)
    return v

def shares_to_word(shares):
    """
    :param shares:
    :return     v:
    """
    v = 0
    for sh in shares:
        v ^= sh
    return v

def word_to_shares(v, nb, ns):
    """
    :param v        : value of word
    :param nb       : bitsize of v
    :param ns       : number of shares
    :return shares  : list of `ns` shares of `v`
    """
    n = 1 << nb

    shares = []
    last_share = v
    for _ in range(ns-1):
        sh = randint(0, n-1)
        last_share ^= sh
        shares.append(sh)
    shares.append(last_share)
    return shares

def word_to_bit_shares(v, nb, ns):
    """
    :param v :
    :param nb:
    :param ns:
    :return  : `ns` shares of 1st bit, `ns` shares of 2nd bit, ... (from LSB to MSB)
    """
    word_shares = word_to_shares(v, nb, ns)
    bit_shares = [word_to_bits(wsh, nb) for wsh in word_shares]

    reordered_bit_shares = []
    for i in range(nb):
        reordered_bit_shares += [bs[i] for bs in bit_shares]
    
    return reordered_bit_shares

def bit_shares_to_word(bit_shares, nb, ns):
    """
    :param bit_shares:
    :param nb        :
    :param ns        :
    :return          : 
    """
    bits = []
    for i in range(nb):
        b = 0
        for j in range(ns):
            b ^= bit_shares[i*ns+j]
        bits.append(b)
    v = bits_to_word(bits, nb)
    return v