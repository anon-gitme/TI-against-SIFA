from outils import mul2, mul4, mul9, mul13
from random import randint

SBOX = [0xC, 0x5, 0x6, 0xB, 0x9, 0x0, 0xA, 0xD, 0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2]
INV_SBOX = [0x5, 0xE, 0xF, 0x8, 0xC, 0x1, 0x2, 0xD, 0xB, 0x4, 0x6, 0x3, 0x0, 0x7, 0x9, 0xA]

RC = [0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3E, 0x3D, 0x3B, 0x37, 0x2F, 0x1E, 0x3C, 0x39, 0x33, 0x27, 0x0E, 0x1D, 0x3A, 0x35, 0x2B, 0x16, 0x2C, 0x18, 0x30,
      0x21, 0x02, 0x05, 0x0B, 0x17, 0x2E, 0x1C, 0x38, 0x31, 0x23, 0x06, 0x0D, 0x1B, 0x36, 0x2D, 0x1A, 0x34, 0x29, 0x12, 0x24, 0x08, 0x11, 0x22, 0x04]

class RawLED:
    def __init__(self, key, DEBUG=False, FAULT=False) -> None:
        '''
        :param key: master key
        '''
        self.DEBUG = DEBUG
        self.FAULT = FAULT
        self.l = len(key)
        self.key_bitsize = self.l * 4
        self.key = key
        assert self.key_bitsize >= 64
        
        # number of steps
        if self.l == 16:
            self.s = 8
        else:
            self.s = 12
        
        self.ks7654 = (self.key_bitsize >> 4) & 0xF
        self.ks3210 = self.key_bitsize & 0xF

        

    def _add_round_key(self, state, i) -> list:
        '''
        :param state: state
        :param i    : step number
        '''
        new_state = [state[j] ^ self.key[(j+i*16) % self.l] for j in range(16)]
        if self.DEBUG:
            sk = [self.key[(j+i*16) % self.l] for j in range(16)]
            print(f"SK : {sk} ({i})")
            print(f"ARK: {new_state}")
        return new_state
    
    def _add_constants(self, state, rn) -> list:
        '''
        :param state: state
        :param rn   : round number
        '''
        new_state = [value for value in state]
        rc543 = (RC[rn] >> 3) & 0x7
        rc210 = (RC[rn]) & 0x7

        new_state[0] ^= (self.ks7654)
        new_state[4] ^= (self.ks7654 ^ 1)
        new_state[8] ^= (self.ks3210 ^ 2)
        new_state[12]^= (self.ks3210 ^ 3)

        new_state[1] ^= rc543
        new_state[5] ^= rc210
        new_state[9] ^= rc543
        new_state[13]^= rc210

        if self.DEBUG:
            print(f"ACS: {new_state}")

        return new_state

    def _sub_cells(self, state, is_faulted) -> list:
        new_state = [SBOX[state[j]] for j in range(16)]

        if self.FAULT and is_faulted and randint(0,1) == 0 and randint(0,1) == 0 and randint(0,1) == 0:
            new_state[0] = 0

        if self.DEBUG:
            print(f"SC : {new_state}")

        return new_state

    def _shift_rows(self, state) -> list:
        new_state = [state[0], state[1], state[2], state[3], 
                     state[5], state[6], state[7], state[4],
                     state[10], state[11], state[8], state[9], 
                     state[15], state[12], state[13], state[14]]

        if self.DEBUG:
            print(f"SR : {new_state}")

        return new_state

    def __mix_a_column(self, col):
        new_col = col
        for _ in range(4):
            new_col = [
                new_col[1],
                new_col[2],
                new_col[3],
                mul4(new_col[0]) ^ new_col[1] ^ mul2(new_col[2]) ^ mul2(new_col[3])
            ]
        return new_col

    def _mix_columns_serial(self, state) -> list:
        col1 = [state[0], state[4], state[8], state[12]]
        col2 = [state[1], state[5], state[9], state[13]]
        col3 = [state[2], state[6], state[10], state[14]]
        col4 = [state[3], state[7], state[11], state[15]]

        new_col1 = self.__mix_a_column(col1)
        new_col2 = self.__mix_a_column(col2)
        new_col3 = self.__mix_a_column(col3)
        new_col4 = self.__mix_a_column(col4)

        new_state = [
            new_col1[0], new_col2[0], new_col3[0], new_col4[0],
            new_col1[1], new_col2[1], new_col3[1], new_col4[1],
            new_col1[2], new_col2[2], new_col3[2], new_col4[2],
            new_col1[3], new_col2[3], new_col3[3], new_col4[3]
        ]
        return new_state

    def _step(self, state, i) -> list:
        '''
        :param state: state
        :param i    : step number
        '''
        new_state = state
        for j in range(4):
            new_state = self._add_constants(new_state, i*4+j)
            new_state = self._sub_cells(new_state, is_faulted = (i*4+j == 47))
            new_state = self._shift_rows(new_state)
            new_state = self._mix_columns_serial(new_state)
        return new_state

    
    def encrypt(self, m) -> list:
        '''
        :param m: plaintext as a list of 16 4-bit elements
        '''

        assert len(m) == 16
        state = m
        for i in range(self.s):
            state = self._add_round_key(state, i)
            state = self._step(state, i)
        state = self._add_round_key(state, i)
        
        return state


###############################################
##### Functions for backward calculations #####
###############################################    
def inv_shift_rows(state):
    new_state = [state[0] , state[1] , state[2] , state[3], 
                 state[7] , state[4] , state[5] , state[6],
                 state[10], state[11], state[8] , state[9], 
                 state[13], state[14], state[15], state[12]]
    return new_state

def inv_mix_a_column(col):
    new_col = col
    for _ in range(4):
        new_col = [
            mul13(new_col[0]) ^ mul9(new_col[1]) ^ mul9(new_col[2]) ^ mul13(new_col[3]),
            new_col[0],
            new_col[1],
            new_col[2]
        ]
    return new_col

def inv_mix_columns_serial(state):
    col1 = [state[0], state[4], state[8], state[12]]
    col2 = [state[1], state[5], state[9], state[13]]
    col3 = [state[2], state[6], state[10], state[14]]
    col4 = [state[3], state[7], state[11], state[15]]

    new_col1 = inv_mix_a_column(col1)
    new_col2 = inv_mix_a_column(col2)
    new_col3 = inv_mix_a_column(col3)
    new_col4 = inv_mix_a_column(col4)

    new_state = [
        new_col1[0], new_col2[0], new_col3[0], new_col4[0],
        new_col1[1], new_col2[1], new_col3[1], new_col4[1],
        new_col1[2], new_col2[2], new_col3[2], new_col4[2],
        new_col1[3], new_col2[3], new_col3[3], new_col4[3]
    ]

    return new_state

def inv_add_round_key(state, key):
    new_state = [state[j] ^ key[j] for j in range(16)]
    return new_state

def inv_sub_cells(state):
    new_state = [INV_SBOX[state[j]] for j in range(16)]
    return new_state

def inv_add_constants(state, rn=47, key_bitsize=128):
    new_state = [value for value in state]
    rc543 = (RC[rn] >> 3) & 0x7
    rc210 = (RC[rn]) & 0x7

    ks7654 = (key_bitsize >> 4) & 0xF
    ks3210 = key_bitsize & 0xF

    new_state[0] ^= (ks7654)
    new_state[4] ^= (ks7654 ^ 1)
    new_state[8] ^= (ks3210 ^ 2)
    new_state[12]^= (ks3210 ^ 3)

    new_state[1] ^= rc543
    new_state[5] ^= rc210
    new_state[9] ^= rc543
    new_state[13]^= rc210

    return new_state