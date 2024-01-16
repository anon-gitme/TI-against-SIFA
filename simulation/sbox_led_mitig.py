from random import randint

def G_1(x12, x13, x22, x23, x32, x33, x42, x43):
    a11 = x22 ^ x32 ^ x42 ^ x12 ^ x23 ^ (x32&x23) ^ (x22&x33) ^ (x23&x33)
    a21 = x12
    a31 = 1 ^ x42 ^ x12 ^ x23 ^ (x32&x23) ^ (x22&x33) ^ (x23&x33)
    a41 = 1 ^ x22 ^ x12 ^ x23 ^ (x32&x23) ^ (x22&x33) ^ (x23&x33) ^ (x42&x23) ^ (x42&x33) ^ (x22&x43) ^ (x32&x43) ^ (x23&x43) ^ (x33&x43)
    return a11, a21, a31, a41

def G_2(x11, x13, x21, x23, x31, x33, x41, x43):
    a12 = x13 ^ x23 ^ x33 ^ x43 ^ x21 ^ (x33&x21) ^ (x23&x31) ^ (x21&x31)
    a22 = x13
    a32 = 1 ^ x13 ^ x43 ^ x21 ^ (x33&x21) ^ (x23&x31) ^ (x21&x31)
    a42 = 1 ^ x13 ^ x23 ^ x21 ^ (x33&x21) ^ (x43&x21) ^ (x23&x31) ^ (x43&x31) ^ (x21&x31) ^ (x23&x41) ^ (x33&x41) ^ (x21&x41) ^ (x31&x41)
    return a12, a22, a32, a42

def G_3(x11, x12, x21, x22, x31, x32, x41, x42):
    a13 = x11 ^ x21 ^ x31 ^ x41 ^ x22 ^ (x31&x22) ^ (x21&x32) ^ (x22&x32)
    a23 = x11
    a33 = 1 ^ x11 ^ x41 ^ x22 ^ (x31&x22) ^ (x21&x32) ^ (x22&x32)
    a43 = 1 ^ x11 ^ x21 ^ x22 ^ (x31&x22) ^ (x41&x22) ^ (x21&x32) ^ (x41&x32) ^ (x22&x32) ^ (x21&x42) ^ (x31&x42) ^ (x22&x42) ^ (x32&x42)
    return a13, a23, a33, a43

def F_1(x12, x13, x22, x23, x32, x33, x42, x43):
    a11 = x12
    a21 = x32 ^ x42 ^ (x42&x23) ^ (x22&x43) ^ (x23&x43)
    a31 = 1 ^ x12 ^ x22 ^ x32 ^ (x42&x33) ^ (x32&x43) ^ (x33&x43)
    a41 = x32 ^ (x42&x23) ^ (x22&x43) ^ (x23&x43)
    return a11, a21, a31, a41

def F_2(x11, x13, x21, x23, x31, x33, x41, x43):
    a12 = x13
    a22 = x33 ^ x43 ^ (x43&x21) ^ (x23&x41) ^ (x21&x41)
    a32 = 1 ^ x13 ^ x23 ^ x33 ^ (x43&x31) ^ (x33&x41) ^ (x31&x41)
    a42 = x33 ^ (x43&x21) ^ (x23&x41) ^ (x21&x41)
    return a12, a22, a32, a42

def F_3(x11, x12, x21, x22, x31, x32, x41, x42):
    a13 = x11
    a23 = x31 ^ x41 ^ (x41&x22) ^ (x21&x42) ^ (x22&x42)
    a33 = 1 ^ x11 ^ x21 ^ x31 ^ (x41&x32) ^ (x31&x42) ^ (x32&x42)
    a43 = x31 ^ (x41&x22) ^ (x21&x42) ^ (x22&x42)
    return a13, a23, a33, a43

def sbox_led_mitigated(x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43):
    y11, y21, y31, y41 = G_1(x12, x13, x22, x23, x32, x33, x42, x43)        
    y12, y22, y32, y42 = G_2(x11, x13, x21, x23, x31, x33, x41, x43)
    y13, y23, y33, y43 = G_3(x11, x12, x21, x22, x31, x32, x41, x42)

    a11, a21, a31, a41 = F_1(y12, y13, y22, y23, y32, y33, y42, y43)
    a12, a22, a32, a42 = F_2(y11, y13, y21, y23, y31, y33, y41, y43)
    a13, a23, a33, a43 = F_3(y11, y12, y21, y22, y31, y32, y41, y42)
    return a11, a12, a13, a21, a22, a23, a31, a32, a33, a41, a42, a43

STUCK_AT_0 = 0
STUCK_AT_1 = 1

############# FAULTS IN REGISTER #############

def sbox_led_mitigated_register_stk0(x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43):
    x11 = STUCK_AT_0
    x12 = STUCK_AT_0
    x21 = STUCK_AT_0
    x22 = STUCK_AT_0
    x31 = STUCK_AT_0
    x32 = STUCK_AT_0
    x41 = STUCK_AT_0
    x42 = STUCK_AT_0
    y11, y21, y31, y41 = G_1(x12, x13, x22, x23, x32, x33, x42, x43)        
    y12, y22, y32, y42 = G_2(x11, x13, x21, x23, x31, x33, x41, x43)
    y13, y23, y33, y43 = G_3(x11, x12, x21, x22, x31, x32, x41, x42)
    a11, a21, a31, a41 = F_1(y12, y13, y22, y23, y32, y33, y42, y43)
    a12, a22, a32, a42 = F_2(y11, y13, y21, y23, y31, y33, y41, y43)
    a13, a23, a33, a43 = F_3(y11, y12, y21, y22, y31, y32, y41, y42)
    return (x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43),\
           (a11, a12, a13, a21, a22, a23, a31, a32, a33, a41, a42, a43)

def sbox_led_mitigated_register_stk1(x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43):
    x11 = STUCK_AT_1
    x12 = STUCK_AT_1
    x21 = STUCK_AT_1
    x22 = STUCK_AT_1
    x31 = STUCK_AT_1
    x32 = STUCK_AT_1
    x41 = STUCK_AT_1
    x42 = STUCK_AT_1
    y11, y21, y31, y41 = G_1(x12, x13, x22, x23, x32, x33, x42, x43)        
    y12, y22, y32, y42 = G_2(x11, x13, x21, x23, x31, x33, x41, x43)
    y13, y23, y33, y43 = G_3(x11, x12, x21, x22, x31, x32, x41, x42)
    a11, a21, a31, a41 = F_1(y12, y13, y22, y23, y32, y33, y42, y43)
    a12, a22, a32, a42 = F_2(y11, y13, y21, y23, y31, y33, y41, y43)
    a13, a23, a33, a43 = F_3(y11, y12, y21, y22, y31, y32, y41, y42)
    return (x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43),\
           (a11, a12, a13, a21, a22, a23, a31, a32, a33, a41, a42, a43)

def sbox_led_mitigated_register_flip(x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43):
    x11 ^= 1
    x12 ^= 1
    x21 ^= 1
    x22 ^= 1
    x31 ^= 1
    x32 ^= 1
    x41 ^= 1
    x42 ^= 1
    y11, y21, y31, y41 = G_1(x12, x13, x22, x23, x32, x33, x42, x43)        
    y12, y22, y32, y42 = G_2(x11, x13, x21, x23, x31, x33, x41, x43)
    y13, y23, y33, y43 = G_3(x11, x12, x21, x22, x31, x32, x41, x42)
    a11, a21, a31, a41 = F_1(y12, y13, y22, y23, y32, y33, y42, y43)
    a12, a22, a32, a42 = F_2(y11, y13, y21, y23, y31, y33, y41, y43)
    a13, a23, a33, a43 = F_3(y11, y12, y21, y22, y31, y32, y41, y42)
    return (x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43),\
           (a11, a12, a13, a21, a22, a23, a31, a32, a33, a41, a42, a43)

def sbox_led_mitigated_register_rand(x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43):
    x11 ^= randint(0, 1)
    x12 ^= randint(0, 1)
    x21 ^= randint(0, 1)
    x22 ^= randint(0, 1)
    x31 ^= randint(0, 1)
    x32 ^= randint(0, 1)
    x41 ^= randint(0, 1)
    x42 ^= randint(0, 1)
    y11, y21, y31, y41 = G_1(x12, x13, x22, x23, x32, x33, x42, x43)        
    y12, y22, y32, y42 = G_2(x11, x13, x21, x23, x31, x33, x41, x43)
    y13, y23, y33, y43 = G_3(x11, x12, x21, x22, x31, x32, x41, x42)
    a11, a21, a31, a41 = F_1(y12, y13, y22, y23, y32, y33, y42, y43)
    a12, a22, a32, a42 = F_2(y11, y13, y21, y23, y31, y33, y41, y43)
    a13, a23, a33, a43 = F_3(y11, y12, y21, y22, y31, y32, y41, y42)
    return (x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43),\
           (a11, a12, a13, a21, a22, a23, a31, a32, a33, a41, a42, a43)

############# FAULTS IN COMPONENT FUNCTION #############

def sbox_led_mitigated_component_function_stk0(x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43):
    y11, y21, y31, y41 = G_1(x12 & STUCK_AT_0, x13 & STUCK_AT_0, x22 & STUCK_AT_0, 
                             x23, x32, x33, x42, x43)        
    y12, y22, y32, y42 = G_2(x11, x13, x21, x23, x31, x33, x41, x43)
    y13, y23, y33, y43 = G_3(x11, x12, x21, x22, x31, x32, x41, x42)
    a11, a21, a31, a41 = F_1(y12, y13, y22, y23, y32, y33, y42, y43)
    a12, a22, a32, a42 = F_2(y11, y13, y21, y23, y31, y33, y41, y43)
    a13, a23, a33, a43 = F_3(y11, y12, y21, y22, y31, y32, y41, y42)
    return a11, a12, a13, a21, a22, a23, a31, a32, a33, a41, a42, a43
           
def sbox_led_mitigated_component_function_stk1(x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43):
    y11, y21, y31, y41 = G_1(x12 | STUCK_AT_1, x13 | STUCK_AT_1, x22 | STUCK_AT_1, 
                             x23, x32, x33, x42, x43)        
    y12, y22, y32, y42 = G_2(x11, x13, x21, x23, x31, x33, x41, x43)
    y13, y23, y33, y43 = G_3(x11, x12, x21, x22, x31, x32, x41, x42)
    a11, a21, a31, a41 = F_1(y12, y13, y22, y23, y32, y33, y42, y43)
    a12, a22, a32, a42 = F_2(y11, y13, y21, y23, y31, y33, y41, y43)
    a13, a23, a33, a43 = F_3(y11, y12, y21, y22, y31, y32, y41, y42)
    return a11, a12, a13, a21, a22, a23, a31, a32, a33, a41, a42, a43

def sbox_led_mitigated_component_function_flip(x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43):
    y11, y21, y31, y41 = G_1(x12, x13 ^ 1, x22, 
                             x23, x32, x33, x42, x43)        
    y12, y22, y32, y42 = G_2(x11, x13, x21, x23, x31, x33, x41, x43)
    y13, y23, y33, y43 = G_3(x11, x12, x21, x22, x31, x32, x41, x42)
    a11, a21, a31, a41 = F_1(y12, y13, y22, y23, y32, y33, y42, y43)
    a12, a22, a32, a42 = F_2(y11, y13, y21, y23, y31, y33, y41, y43)
    a13, a23, a33, a43 = F_3(y11, y12, y21, y22, y31, y32, y41, y42)
    return a11, a12, a13, a21, a22, a23, a31, a32, a33, a41, a42, a43

def sbox_led_mitigated_component_function_rand(x11, x12, x13, x21, x22, x23, x31, x32, x33, x41, x42, x43):
    y11, y21, y31, y41 = G_1(x12 ^ randint(0, 1), x13 ^ randint(0,1), x22, 
                             x23, x32, x33, x42, x43)        
    y12, y22, y32, y42 = G_2(x11, x13, x21, x23, x31, x33, x41, x43)
    y13, y23, y33, y43 = G_3(x11, x12, x21, x22, x31, x32, x41, x42)
    a11, a21, a31, a41 = F_1(y12, y13, y22, y23, y32, y33, y42, y43)
    a12, a22, a32, a42 = F_2(y11, y13, y21, y23, y31, y33, y41, y43)
    a13, a23, a33, a43 = F_3(y11, y12, y21, y22, y31, y32, y41, y42)
    return a11, a12, a13, a21, a22, a23, a31, a32, a33, a41, a42, a43