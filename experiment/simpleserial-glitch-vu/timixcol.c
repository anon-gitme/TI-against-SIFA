#include "timixcol.h"

// MixColumnSerial for 1st column and j-th share
void mc1(BIT64 *sj){
  BIT16 z;
  // b0  b1  b2  b3  -> x4: b2  b0^b3 b0^b1 b1
  // b16 b17 b18 b19 
  // b32 b33 b34 b35 -> x2: b33 b34 b32^b35 b32
  // b48 b49 b50 b51 -> x2: b49 b50 b48^b51 b48
  for (u8 i=0; i<4; i++){
    z.b0  = (*sj).b16;
    z.b1  = (*sj).b17;
    z.b2  = (*sj).b18;
    z.b3  = (*sj).b19;

    z.b4  = (*sj).b32;
    z.b5  = (*sj).b33;
    z.b6  = (*sj).b34;
    z.b7  = (*sj).b35;

    z.b8  = (*sj).b48;
    z.b9  = (*sj).b49;
    z.b10 = (*sj).b50;
    z.b11 = (*sj).b51;

    z.b12 = (*sj).b2 ^ (*sj).b16 ^ (*sj).b33 ^ (*sj).b49;
    z.b13 = (*sj).b0 ^ (*sj).b3  ^ (*sj).b17 ^ (*sj).b34 ^ (*sj).b50;
    z.b14 = (*sj).b0 ^ (*sj).b1  ^ (*sj).b18 ^ (*sj).b32 ^ (*sj).b35 ^ (*sj).b48 ^ (*sj).b51;
    z.b15 = (*sj).b1 ^ (*sj).b19 ^ (*sj).b32 ^ (*sj).b48;
  
    (*sj).b0  = z.b0;
    (*sj).b1  = z.b1;
    (*sj).b2  = z.b2;
    (*sj).b3  = z.b3;

    (*sj).b16 = z.b4;
    (*sj).b17 = z.b5;
    (*sj).b18 = z.b6;
    (*sj).b19 = z.b7;

    (*sj).b32 = z.b8;
    (*sj).b33 = z.b9;
    (*sj).b34 = z.b10;
    (*sj).b35 = z.b11;    

    (*sj).b48 = z.b12;
    (*sj).b49 = z.b13;
    (*sj).b50 = z.b14;
    (*sj).b51 = z.b15;
  }
}

// MixColumnSerial for 2nd column and j-th share
void mc2(BIT64 *sj){
  BIT16 z;
  // b0  b1  b2  b3  -> x4: b2  b0^b3 b0^b1 b1
  // b16 b17 b18 b19 
  // b32 b33 b34 b35 -> x2: b33 b34 b32^b35 b32
  // b48 b49 b50 b51 -> x2: b49 b50 b48^b51 b48
  for (u8 i=0; i<4; i++){
    z.b0  = (*sj).b20;
    z.b1  = (*sj).b21;
    z.b2  = (*sj).b22;
    z.b3  = (*sj).b23;

    z.b4  = (*sj).b36;
    z.b5  = (*sj).b37;
    z.b6  = (*sj).b38;
    z.b7  = (*sj).b39;

    z.b8  = (*sj).b52;
    z.b9  = (*sj).b53;
    z.b10 = (*sj).b54;
    z.b11 = (*sj).b55;

    z.b12 = (*sj).b6 ^ (*sj).b20 ^ (*sj).b37 ^ (*sj).b53;
    z.b13 = (*sj).b4 ^ (*sj).b7  ^ (*sj).b21 ^ (*sj).b38 ^ (*sj).b54;
    z.b14 = (*sj).b4 ^ (*sj).b5  ^ (*sj).b22 ^ (*sj).b36 ^ (*sj).b39 ^ (*sj).b52 ^ (*sj).b55;
    z.b15 = (*sj).b5 ^ (*sj).b23 ^ (*sj).b36 ^ (*sj).b52;
  
    (*sj).b4  = z.b0;
    (*sj).b5  = z.b1;
    (*sj).b6  = z.b2;
    (*sj).b7  = z.b3;

    (*sj).b20 = z.b4;
    (*sj).b21 = z.b5;
    (*sj).b22 = z.b6;
    (*sj).b23 = z.b7;

    (*sj).b36 = z.b8;
    (*sj).b37 = z.b9;
    (*sj).b38 = z.b10;
    (*sj).b39 = z.b11;    

    (*sj).b52 = z.b12;
    (*sj).b53 = z.b13;
    (*sj).b54 = z.b14;
    (*sj).b55 = z.b15;
  }
}

// MixColumnSerial for 3rd column and j-th share
void mc3(BIT64 *sj){
  BIT16 z;
  // b0  b1  b2  b3  -> x4: b2  b0^b3 b0^b1 b1
  // b16 b17 b18 b19 
  // b32 b33 b34 b35 -> x2: b33 b34 b32^b35 b32
  // b48 b49 b50 b51 -> x2: b49 b50 b48^b51 b48
  for (u8 i=0; i<4; i++){
    z.b0  = (*sj).b24;
    z.b1  = (*sj).b25;
    z.b2  = (*sj).b26;
    z.b3  = (*sj).b27;

    z.b4  = (*sj).b40;
    z.b5  = (*sj).b41;
    z.b6  = (*sj).b42;
    z.b7  = (*sj).b43;

    z.b8  = (*sj).b56;
    z.b9  = (*sj).b57;
    z.b10 = (*sj).b58;
    z.b11 = (*sj).b59;

    z.b12 = (*sj).b10 ^ (*sj).b24 ^ (*sj).b41 ^ (*sj).b57;
    z.b13 = (*sj).b8  ^ (*sj).b11 ^ (*sj).b25 ^ (*sj).b42 ^ (*sj).b58;
    z.b14 = (*sj).b8  ^ (*sj).b9  ^ (*sj).b26 ^ (*sj).b40 ^ (*sj).b43 ^ (*sj).b56 ^ (*sj).b59;
    z.b15 = (*sj).b9  ^ (*sj).b27 ^ (*sj).b40 ^ (*sj).b56;
  
    (*sj).b8  = z.b0;
    (*sj).b9  = z.b1;
    (*sj).b10 = z.b2;
    (*sj).b11 = z.b3;

    (*sj).b24 = z.b4;
    (*sj).b25 = z.b5;
    (*sj).b26 = z.b6;
    (*sj).b27 = z.b7;

    (*sj).b40 = z.b8;
    (*sj).b41 = z.b9;
    (*sj).b42 = z.b10;
    (*sj).b43 = z.b11;    

    (*sj).b56 = z.b12;
    (*sj).b57 = z.b13;
    (*sj).b58 = z.b14;
    (*sj).b59 = z.b15;
  }
}

// MixColumnSerial for 4nd column and j-th share
void mc4(BIT64 *sj){
  BIT16 z;
  // b0  b1  b2  b3  -> x4: b2  b0^b3 b0^b1 b1
  // b16 b17 b18 b19 
  // b32 b33 b34 b35 -> x2: b33 b34 b32^b35 b32
  // b48 b49 b50 b51 -> x2: b49 b50 b48^b51 b48
  for (u8 i=0; i<4; i++){
    z.b0  = (*sj).b28;
    z.b1  = (*sj).b29;
    z.b2  = (*sj).b30;
    z.b3  = (*sj).b31;

    z.b4  = (*sj).b44;
    z.b5  = (*sj).b45;
    z.b6  = (*sj).b46;
    z.b7  = (*sj).b47;

    z.b8  = (*sj).b60;
    z.b9  = (*sj).b61;
    z.b10 = (*sj).b62;
    z.b11 = (*sj).b63;

    z.b12 = (*sj).b14 ^ (*sj).b28 ^ (*sj).b45 ^ (*sj).b61;
    z.b13 = (*sj).b12 ^ (*sj).b15 ^ (*sj).b29 ^ (*sj).b46 ^ (*sj).b62;
    z.b14 = (*sj).b12 ^ (*sj).b13 ^ (*sj).b30 ^ (*sj).b44 ^ (*sj).b47 ^ (*sj).b60 ^ (*sj).b63;
    z.b15 = (*sj).b13 ^ (*sj).b31 ^ (*sj).b44 ^ (*sj).b60;
  
    (*sj).b12 = z.b0;
    (*sj).b13 = z.b1;
    (*sj).b14 = z.b2;
    (*sj).b15 = z.b3;

    (*sj).b28 = z.b4;
    (*sj).b29 = z.b5;
    (*sj).b30 = z.b6;
    (*sj).b31 = z.b7;

    (*sj).b44 = z.b8;
    (*sj).b45 = z.b9;
    (*sj).b46 = z.b10;
    (*sj).b47 = z.b11;    

    (*sj).b60 = z.b12;
    (*sj).b61 = z.b13;
    (*sj).b62 = z.b14;
    (*sj).b63 = z.b15;
  }
}
