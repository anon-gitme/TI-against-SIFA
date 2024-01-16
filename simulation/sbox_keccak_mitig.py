from random import randint
STUCK_AT_0 = 0
STUCK_AT_1 = 1

def a_0(x01, x02, x03, x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43):
    a00 = x01 ^ x21 ^ (x11 ^ x12 ^ x13) & (x21 ^ x22 ^ x23)
    a10 = x11 ^ x31 ^ (x21 ^ x22 ^ x23) & (x31 ^ x32 ^ x33)
    a20 = x21 ^ x41 ^ (x31 ^ x32 ^ x33) & (x41 ^ x42 ^ x43)
    a30 = x31 ^ x01 ^ x02 ^ x03 ^ (x41 ^ x42 ^ x43) & (x01 ^ x02 ^ x03)
    a40 = x41 ^ x11 ^ (x01 ^ x02 ^ x03) & (x11 ^ x12 ^ x13)
    return a00, a10, a20, a30, a40

def a_1(x00, x02, x03, x10, x12, x13, x20, x22, x23, x30, x32, x33, x40, x42, x43):
    a01 = x02 ^ x22 ^ (x10 & (x22 ^ x23) ^ x20 & (x12 ^ x13) ^ x10 & x20)
    a11 = x12 ^ x32 ^ (x20 & (x32 ^ x33) ^ x30 & (x22 ^ x23) ^ x20 & x30)
    a21 = x22 ^ x42 ^ (x30 & (x42 ^ x43) ^ x40 & (x32 ^ x33) ^ x30 & x40)
    a31 = x32 ^ x00 ^ (x40 & (x02 ^ x03) ^ x00 & (x42 ^ x43) ^ x40 & x00)
    a41 = x42 ^ x12 ^ (x00 & (x12 ^ x13) ^ x10 & (x02 ^ x03) ^ x00 & x10)
    return a01, a11, a21, a31, a41

def a_2(x00, x01, x03, x10, x11, x13, x20, x21, x23, x30, x31, x33, x40, x41, x43):
    a02 = x03 ^ x23 ^ (x10 & x21 ^ x20 & x11)
    a12 = x13 ^ x33 ^ (x20 & x31 ^ x30 & x21)
    a22 = x23 ^ x43 ^ (x30 & x41 ^ x40 & x31)
    a32 = x33 ^ (x40 & x01 ^ x00 & x41)
    a42 = x43 ^ x13 ^ (x00 & x11 ^ x10 & x01)
    return a02, a12, a22, a32, a42

def a_3(x00, x01, x02, x10, x11, x12, x20, x21, x22, x30, x31, x32, x40, x41, x42):
    a03 = x00 ^ x20
    a13 = x10 ^ x30
    a23 = x20 ^ x40
    a33 = x30
    a43 = x40 ^ x10
    return a03, a13, a23, a33, a43

def sbox_keccak_mitigated(x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43):
    a00, a10, a20, a30, a40 = a_0(x01, x02, x03, x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43)
    a01, a11, a21, a31, a41 = a_1(x00, x02, x03, x10, x12, x13, x20, x22, x23, x30, x32, x33, x40, x42, x43)
    a02, a12, a22, a32, a42 = a_2(x00, x01, x03, x10, x11, x13, x20, x21, x23, x30, x31, x33, x40, x41, x43)
    a03, a13, a23, a33, a43 = a_3(x00, x01, x02, x10, x11, x12, x20, x21, x22, x30, x31, x32, x40, x41, x42)
    return a00, a01, a02, a03, a10, a11, a12, a13, a20, a21, a22, a23, a30, a31, a32, a33, a40, a41, a42, a43

##############################################
############# FAULTS IN REGISTER #############
##############################################

def sbox_keccak_mitigated_register_stk0(x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43):    
    x00 = STUCK_AT_0
    x01 = STUCK_AT_0
    x02 = STUCK_AT_0
    x10 = STUCK_AT_0
    x11 = STUCK_AT_0
    x12 = STUCK_AT_0
    x20 = STUCK_AT_0
    x21 = STUCK_AT_0
    x22 = STUCK_AT_0
    x30 = STUCK_AT_0
    x31 = STUCK_AT_0
    x32 = STUCK_AT_0
    x40 = STUCK_AT_0
    x41 = STUCK_AT_0
    x42 = STUCK_AT_0
    
    a00, a10, a20, a30, a40 = a_0(x01, x02, x03, x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43)
    a01, a11, a21, a31, a41 = a_1(x00, x02, x03, x10, x12, x13, x20, x22, x23, x30, x32, x33, x40, x42, x43)
    a02, a12, a22, a32, a42 = a_2(x00, x01, x03, x10, x11, x13, x20, x21, x23, x30, x31, x33, x40, x41, x43)
    a03, a13, a23, a33, a43 = a_3(x00, x01, x02, x10, x11, x12, x20, x21, x22, x30, x31, x32, x40, x41, x42)    
    return (x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43),\
           (a00, a01, a02, a03, a10, a11, a12, a13, a20, a21, a22, a23, a30, a31, a32, a33, a40, a41, a42, a43)

def sbox_keccak_mitigated_register_stk1(x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43):    
    x00 = STUCK_AT_1
    x01 = STUCK_AT_1
    x02 = STUCK_AT_1
    x10 = STUCK_AT_1
    x11 = STUCK_AT_1
    x12 = STUCK_AT_1
    x20 = STUCK_AT_1
    x21 = STUCK_AT_1
    x22 = STUCK_AT_1
    x30 = STUCK_AT_1
    x31 = STUCK_AT_1
    x32 = STUCK_AT_1
    x40 = STUCK_AT_1
    x41 = STUCK_AT_1
    x42 = STUCK_AT_1
    
    a00, a10, a20, a30, a40 = a_0(x01, x02, x03, x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43)
    a01, a11, a21, a31, a41 = a_1(x00, x02, x03, x10, x12, x13, x20, x22, x23, x30, x32, x33, x40, x42, x43)
    a02, a12, a22, a32, a42 = a_2(x00, x01, x03, x10, x11, x13, x20, x21, x23, x30, x31, x33, x40, x41, x43)
    a03, a13, a23, a33, a43 = a_3(x00, x01, x02, x10, x11, x12, x20, x21, x22, x30, x31, x32, x40, x41, x42)    
    return (x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43),\
           (a00, a01, a02, a03, a10, a11, a12, a13, a20, a21, a22, a23, a30, a31, a32, a33, a40, a41, a42, a43)

def sbox_keccak_mitigated_register_flip(x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43):    
    x02 ^= 1

    a00, a10, a20, a30, a40 = a_0(x01, x02, x03, x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43)
    a01, a11, a21, a31, a41 = a_1(x00, x02, x03, x10, x12, x13, x20, x22, x23, x30, x32, x33, x40, x42, x43)
    a02, a12, a22, a32, a42 = a_2(x00, x01, x03, x10, x11, x13, x20, x21, x23, x30, x31, x33, x40, x41, x43)
    a03, a13, a23, a33, a43 = a_3(x00, x01, x02, x10, x11, x12, x20, x21, x22, x30, x31, x32, x40, x41, x42)    
    return (x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43),\
           (a00, a01, a02, a03, a10, a11, a12, a13, a20, a21, a22, a23, a30, a31, a32, a33, a40, a41, a42, a43)

def sbox_keccak_mitigated_register_rand(x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43):    
    x00 ^= randint(0, 1)
    x01 ^= randint(0, 1)
    x02 ^= randint(0, 1)
    x10 ^= randint(0, 1)
    x11 ^= randint(0, 1)
    x12 ^= randint(0, 1)
    x20 ^= randint(0, 1)
    x21 ^= randint(0, 1)
    x22 ^= randint(0, 1)
    x30 ^= randint(0, 1)
    x31 ^= randint(0, 1)
    x32 ^= randint(0, 1)
    x40 ^= randint(0, 1)
    x41 ^= randint(0, 1)
    x42 ^= randint(0, 1)
    
    a00, a10, a20, a30, a40 = a_0(x01, x02, x03, x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43)
    a01, a11, a21, a31, a41 = a_1(x00, x02, x03, x10, x12, x13, x20, x22, x23, x30, x32, x33, x40, x42, x43)
    a02, a12, a22, a32, a42 = a_2(x00, x01, x03, x10, x11, x13, x20, x21, x23, x30, x31, x33, x40, x41, x43)
    a03, a13, a23, a33, a43 = a_3(x00, x01, x02, x10, x11, x12, x20, x21, x22, x30, x31, x32, x40, x41, x42)    
    return (x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43),\
           (a00, a01, a02, a03, a10, a11, a12, a13, a20, a21, a22, a23, a30, a31, a32, a33, a40, a41, a42, a43)

########################################################
############# FAULTS IN COMPONENT FUNCTION #############
########################################################

def sbox_keccak_mitigated_cfunc_stk0(x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43):    
    a00, a10, a20, a30, a40 = a_0(x01 & STUCK_AT_0, x02 & STUCK_AT_0, x03 & STUCK_AT_0, 
                                  x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43)
    a01, a11, a21, a31, a41 = a_1(x00, x02, x03, x10, x12, x13, x20, x22, x23, x30, x32, x33, x40, x42, x43)
    a02, a12, a22, a32, a42 = a_2(x00, x01, x03, x10, x11, x13, x20, x21, x23, x30, x31, x33, x40, x41, x43)
    a03, a13, a23, a33, a43 = a_3(x00, x01, x02, x10, x11, x12, x20, x21, x22, x30, x31, x32, x40, x41, x42)    
    return a00, a01, a02, a03, a10, a11, a12, a13, a20, a21, a22, a23, a30, a31, a32, a33, a40, a41, a42, a43

def sbox_keccak_mitigated_cfunc_stk1(x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43):    
    a00, a10, a20, a30, a40 = a_0(x01 | STUCK_AT_1, x02 | STUCK_AT_1, x03 | STUCK_AT_1, 
                                  x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43)
    a01, a11, a21, a31, a41 = a_1(x00, x02, x03, x10, x12, x13, x20, x22, x23, x30, x32, x33, x40, x42, x43)
    a02, a12, a22, a32, a42 = a_2(x00, x01, x03, x10, x11, x13, x20, x21, x23, x30, x31, x33, x40, x41, x43)
    a03, a13, a23, a33, a43 = a_3(x00, x01, x02, x10, x11, x12, x20, x21, x22, x30, x31, x32, x40, x41, x42)    
    return a00, a01, a02, a03, a10, a11, a12, a13, a20, a21, a22, a23, a30, a31, a32, a33, a40, a41, a42, a43

def sbox_keccak_mitigated_cfunc_flip(x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43):    
    a00, a10, a20, a30, a40 = a_0(x01, x02 ^ 1, x03, 
                                  x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43)
    a01, a11, a21, a31, a41 = a_1(x00, x02, x03, x10, x12, x13, x20, x22, x23, x30, x32, x33, x40, x42, x43)
    a02, a12, a22, a32, a42 = a_2(x00, x01, x03, x10, x11, x13, x20, x21, x23, x30, x31, x33, x40, x41, x43)
    a03, a13, a23, a33, a43 = a_3(x00, x01, x02, x10, x11, x12, x20, x21, x22, x30, x31, x32, x40, x41, x42)    
    return a00, a01, a02, a03, a10, a11, a12, a13, a20, a21, a22, a23, a30, a31, a32, a33, a40, a41, a42, a43

def sbox_keccak_mitigated_cfunc_rand(x00, x01, x02, x03, x10, x11, x12, x13, x20, x21, x22, x23, x30, x31, x32, x33, x40, x41, x42, x43):    
    a00, a10, a20, a30, a40 = a_0(x01 ^ randint(0, 1), x02 ^ randint(0, 1), x03 ^ randint(0, 1), 
                                  x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43)
    a01, a11, a21, a31, a41 = a_1(x00, x02, x03, x10, x12, x13, x20, x22, x23, x30, x32, x33, x40, x42, x43)
    a02, a12, a22, a32, a42 = a_2(x00, x01, x03, x10, x11, x13, x20, x21, x23, x30, x31, x33, x40, x41, x43)
    a03, a13, a23, a33, a43 = a_3(x00, x01, x02, x10, x11, x12, x20, x21, x22, x30, x31, x32, x40, x41, x42)    
    return a00, a01, a02, a03, a10, a11, a12, a13, a20, a21, a22, a23, a30, a31, a32, a33, a40, a41, a42, a43