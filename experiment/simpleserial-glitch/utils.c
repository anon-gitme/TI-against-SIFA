#include <stdio.h>
#include <stdlib.h>
#include "utils.h"

void print_sh_state(u64 sh_s[3]){
  printf("1st share: %016llX\n", sh_s[0]);
  printf("2nd share: %016llX\n", sh_s[1]);
  printf("3rd share: %016llX\n", sh_s[2]);
  printf("unshared : %016llX\n", sh_s[0] ^ sh_s[1] ^ sh_s[2]);
}

// Attention! This PRG is not secure!
// rand() in [0, 2^31)
u64 rand64(){
  return ((u64) rand() << 33) | ((u64) rand() << 2) | (rand() & 0x3);  
}

void sh_encode(u64 sh[3], u64 v){
  sh[0] = rand64();
  sh[1] = rand64();
  sh[2] = sh[0] ^ sh[1] ^ v;
}

u64 sh_decode(u64 sh[3]){
  return sh[0] ^ sh[1] ^ sh[2];
}

void sh_key_encode(u64 sh[6], u64 k[2]){
  sh[0] = rand64();
  sh[1] = rand64();
  sh[2] = sh[0] ^ sh[1] ^ k[0];
  sh[3] = rand64();
  sh[4] = rand64();
  sh[5] = sh[3] ^ sh[4] ^ k[1];
}

void u64_to_u8(u8 a[8], u64 x){
  a[0] = (x >> 56) & 0xFF;
  a[1] = (x >> 48) & 0xFF;
  a[2] = (x >> 40) & 0xFF;
  a[3] = (x >> 32) & 0xFF;
  a[4] = (x >> 24) & 0xFF;
  a[5] = (x >> 16) & 0xFF;
  a[6] = (x >>  8) & 0xFF;
  a[7] = (x      ) & 0xFF;
}

void u8_to_u64(u64 *a, u8 x[8]){
  *a = 0;
  *a |= (((u64) x[0]) << 56);
  *a |= (((u64) x[1]) << 48);
  *a |= (((u64) x[2]) << 40);
  *a |= (((u64) x[3]) << 32);
  *a |= (((u64) x[4]) << 24);
  *a |= (((u64) x[5]) << 16);
  *a |= (((u64) x[6]) <<  8);
  *a |= (((u64) x[7])      );
}