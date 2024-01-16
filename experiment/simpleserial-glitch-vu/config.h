#ifndef _CONFIG_H
#define _CONFIG_H

typedef unsigned long long u64;
typedef unsigned char u8;
typedef unsigned short u16;

// Two halves of byte
typedef struct __attribute__((__packed__)) HBYTE{
    u8 c1  : 4;
    u8 c0  : 4;
} HBYTE;

// 8 bits of a byte
typedef struct __attribute__((__packed__)) BIT8{
    u8 b7  : 1;
    u8 b6  : 1;
    u8 b5  : 1;
    u8 b4  : 1;
    u8 b3  : 1;
    u8 b2  : 1;
    u8 b1  : 1;
    u8 b0  : 1;
} BIT8;

// Nibbles of 4-bit elements
typedef struct __attribute__((__packed__)) NIB4{
    u64 n15 : 4;
    u64 n14 : 4;
    u64 n13 : 4;
    u64 n12 : 4;
    u64 n11 : 4;
    u64 n10 : 4;
    u64 n9  : 4;
    u64 n8  : 4;
    u64 n7  : 4;
    u64 n6  : 4;
    u64 n5  : 4;
    u64 n4  : 4;
    u64 n3  : 4;
    u64 n2  : 4;
    u64 n1  : 4;
    u64 n0  : 4;
} NIB4;

// 64 bits of state
typedef struct __attribute__((__packed__)) BIT64{
    u64 b63 : 1;
    u64 b62 : 1;
    u64 b61 : 1;
    u64 b60 : 1;
    u64 b59 : 1;
    u64 b58 : 1;
    u64 b57 : 1;
    u64 b56 : 1;
    u64 b55 : 1;
    u64 b54 : 1;
    u64 b53 : 1;
    u64 b52 : 1;
    u64 b51 : 1;
    u64 b50 : 1;
    u64 b49 : 1;
    u64 b48 : 1;
    u64 b47 : 1;
    u64 b46 : 1;
    u64 b45 : 1;
    u64 b44 : 1;
    u64 b43 : 1;
    u64 b42 : 1;
    u64 b41 : 1;
    u64 b40 : 1;
    u64 b39 : 1;
    u64 b38 : 1;
    u64 b37 : 1;
    u64 b36 : 1;
    u64 b35 : 1;
    u64 b34 : 1;
    u64 b33 : 1;
    u64 b32 : 1;
    u64 b31 : 1;
    u64 b30 : 1;
    u64 b29 : 1;
    u64 b28 : 1;
    u64 b27 : 1;
    u64 b26 : 1;
    u64 b25 : 1;
    u64 b24 : 1;
    u64 b23 : 1;
    u64 b22 : 1;
    u64 b21 : 1;
    u64 b20 : 1;
    u64 b19 : 1;
    u64 b18 : 1;
    u64 b17 : 1;
    u64 b16 : 1;
    u64 b15 : 1;
    u64 b14 : 1;
    u64 b13 : 1;
    u64 b12 : 1;
    u64 b11 : 1;
    u64 b10 : 1;
    u64 b9  : 1;
    u64 b8  : 1;
    u64 b7  : 1;
    u64 b6  : 1;
    u64 b5  : 1;
    u64 b4  : 1;
    u64 b3  : 1;
    u64 b2  : 1;
    u64 b1  : 1;
    u64 b0  : 1;
} BIT64;

// 64 bits of state
typedef struct __attribute__((__packed__)) BIT16{
    u16 b15 : 1;
    u16 b14 : 1;
    u16 b13 : 1;
    u16 b12 : 1;
    u16 b11 : 1;
    u16 b10 : 1;
    u16 b9  : 1;
    u16 b8  : 1;
    u16 b7  : 1;
    u16 b6  : 1;
    u16 b5  : 1;
    u16 b4  : 1;
    u16 b3  : 1;
    u16 b2  : 1;
    u16 b1  : 1;
    u16 b0  : 1;
} BIT16;

#endif