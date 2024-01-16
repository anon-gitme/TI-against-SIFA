#include "config.h"

void print_sh_state(u64 sh_s[3]);
void sh_encode(u64 sh[3], u64 v);
u64 sh_decode(u64 sh[3]);
void sh_key_encode(u64 sh[6], u64 k[2]);
void u64_to_u8(u8 a[8], u64 x);
void u8_to_u64(u64 *a, u8 x[8]);