#include "vu_tisbox.h"
#include "timixcol.h"
#include "vu_tiled.h"
// #include "utils.h"

void ti_sc(BIT64 *s, u8 is_faulted){
  BIT64 y[3];

  // TI computation for 0-th element
  G_0_b3(y, s);
  G_0_b2(y, s);
  G_0_b1(y, s);
  G_0_b0(y, s, is_faulted);
  F_0_b3(s, y);
  F_0_b2(s, y);
  F_0_b1(s, y);
  F_0_b0(s, y);

  // TI computation for 1-th element
  G_1_b3(y, s);
  G_1_b2(y, s);
  G_1_b1(y, s);
  G_1_b0(y, s);
  F_1_b3(s, y);
  F_1_b2(s, y);
  F_1_b1(s, y);
  F_1_b0(s, y);

  // TI computation for 2-th element
  G_2_b3(y, s);
  G_2_b2(y, s);
  G_2_b1(y, s);
  G_2_b0(y, s);
  F_2_b3(s, y);
  F_2_b2(s, y);
  F_2_b1(s, y);
  F_2_b0(s, y);

  // TI computation for 3-th element
  G_3_b3(y, s);
  G_3_b2(y, s);
  G_3_b1(y, s);
  G_3_b0(y, s);
  F_3_b3(s, y);
  F_3_b2(s, y);
  F_3_b1(s, y);
  F_3_b0(s, y);

  // TI computation for 4-th element
  G_4_b3(y, s);
  G_4_b2(y, s);
  G_4_b1(y, s);
  G_4_b0(y, s);
  F_4_b3(s, y);
  F_4_b2(s, y);
  F_4_b1(s, y);
  F_4_b0(s, y);

  // TI computation for 5-th element
  G_5_b3(y, s);
  G_5_b2(y, s);
  G_5_b1(y, s);
  G_5_b0(y, s);
  F_5_b3(s, y);
  F_5_b2(s, y);
  F_5_b1(s, y);
  F_5_b0(s, y);

  // TI computation for 6-th element
  G_6_b3(y, s);
  G_6_b2(y, s);
  G_6_b1(y, s);
  G_6_b0(y, s);
  F_6_b3(s, y);
  F_6_b2(s, y);
  F_6_b1(s, y);
  F_6_b0(s, y);

  // TI computation for 7-th element
  G_7_b3(y, s);
  G_7_b2(y, s);
  G_7_b1(y, s);
  G_7_b0(y, s);
  F_7_b3(s, y);
  F_7_b2(s, y);
  F_7_b1(s, y);
  F_7_b0(s, y);

  // TI computation for 8-th element
  G_8_b3(y, s);
  G_8_b2(y, s);
  G_8_b1(y, s);
  G_8_b0(y, s);
  F_8_b3(s, y);
  F_8_b2(s, y);
  F_8_b1(s, y);
  F_8_b0(s, y);

  // TI computation for 9-th element
  G_9_b3(y, s);
  G_9_b2(y, s);
  G_9_b1(y, s);
  G_9_b0(y, s);
  F_9_b3(s, y);
  F_9_b2(s, y);
  F_9_b1(s, y);
  F_9_b0(s, y);

  // TI computation for 10-th element
  G_10_b3(y, s);
  G_10_b2(y, s);
  G_10_b1(y, s);
  G_10_b0(y, s);
  F_10_b3(s, y);
  F_10_b2(s, y);
  F_10_b1(s, y);
  F_10_b0(s, y);

  // TI computation for 11-th element
  G_11_b3(y, s);
  G_11_b2(y, s);
  G_11_b1(y, s);
  G_11_b0(y, s);
  F_11_b3(s, y);
  F_11_b2(s, y);
  F_11_b1(s, y);
  F_11_b0(s, y);

  // TI computation for 12-th element
  G_12_b3(y, s);
  G_12_b2(y, s);
  G_12_b1(y, s);
  G_12_b0(y, s);
  F_12_b3(s, y);
  F_12_b2(s, y);
  F_12_b1(s, y);
  F_12_b0(s, y);

  // TI computation for 13-th element
  G_13_b3(y, s);
  G_13_b2(y, s);
  G_13_b1(y, s);
  G_13_b0(y, s);
  F_13_b3(s, y);
  F_13_b2(s, y);
  F_13_b1(s, y);
  F_13_b0(s, y);

  // TI computation for 14-th element
  G_14_b3(y, s);
  G_14_b2(y, s);
  G_14_b1(y, s);
  G_14_b0(y, s);
  F_14_b3(s, y);
  F_14_b2(s, y);
  F_14_b1(s, y);
  F_14_b0(s, y);

  // TI computation for 15-th element
  G_15_b3(y, s);
  G_15_b2(y, s);
  G_15_b1(y, s);
  G_15_b0(y, s);
  F_15_b3(s, y);
  F_15_b2(s, y);
  F_15_b1(s, y);
  F_15_b0(s, y);
}


static void ti_mc(BIT64 *s){
  // Column 1 for 3 shares
  mc1(&s[0]);
  mc1(&s[1]);
  mc1(&s[2]);

  // Column 2 for 3 shares
  mc2(&s[0]);
  mc2(&s[1]);
  mc2(&s[2]);

  // Column 3 for 3 shares
  mc3(&s[0]);
  mc3(&s[1]);
  mc3(&s[2]);

  // Column 3 for 3 shares
  mc4(&s[0]);
  mc4(&s[1]);
  mc4(&s[2]);
}

static void ti_sr(NIB4 *so, const NIB4 *s){
  NIB4 z[3];
  z[0] = s[0]; z[1] = s[1]; z[2] = s[2];
  so[0].n0  = z[0].n0 ; so[0].n1  = z[0].n1 ; so[0].n2  = z[0].n2 ; so[0].n3  = z[0].n3 ;
  so[0].n4  = z[0].n5 ; so[0].n5  = z[0].n6 ; so[0].n6  = z[0].n7 ; so[0].n7  = z[0].n4 ;
  so[0].n8  = z[0].n10; so[0].n9  = z[0].n11; so[0].n10 = z[0].n8 ; so[0].n11 = z[0].n9 ;
  so[0].n12 = z[0].n15; so[0].n13 = z[0].n12; so[0].n14 = z[0].n13; so[0].n15 = z[0].n14;
  so[1].n0  = z[1].n0 ; so[1].n1  = z[1].n1 ; so[1].n2  = z[1].n2 ; so[1].n3  = z[1].n3 ;
  so[1].n4  = z[1].n5 ; so[1].n5  = z[1].n6 ; so[1].n6  = z[1].n7 ; so[1].n7  = z[1].n4 ;
  so[1].n8  = z[1].n10; so[1].n9  = z[1].n11; so[1].n10 = z[1].n8 ; so[1].n11 = z[1].n9 ;
  so[1].n12 = z[1].n15; so[1].n13 = z[1].n12; so[1].n14 = z[1].n13; so[1].n15 = z[1].n14;
  so[2].n0  = z[2].n0 ; so[2].n1  = z[2].n1 ; so[2].n2  = z[2].n2 ; so[2].n3  = z[2].n3 ;
  so[2].n4  = z[2].n5 ; so[2].n5  = z[2].n6 ; so[2].n6  = z[2].n7 ; so[2].n7  = z[2].n4 ;
  so[2].n8  = z[2].n10; so[2].n9  = z[2].n11; so[2].n10 = z[2].n8 ; so[2].n11 = z[2].n9 ;
  so[2].n12 = z[2].n15; so[2].n13 = z[2].n12; so[2].n14 = z[2].n13; so[2].n15 = z[2].n14;
}

const HBYTE RC[48] = {
  {0x1, 0x0}, {0x3, 0x0}, {0x7, 0x0}, {0x7, 0x1}, {0x7, 0x3}, {0x6, 0x7}, {0x5, 0x7}, {0x3, 0x7},
  {0x7, 0x6}, {0x7, 0x5}, {0x6, 0x3}, {0x4, 0x7}, {0x1, 0x7}, {0x3, 0x6}, {0x7, 0x4}, {0x6, 0x1},
  {0x5, 0x3}, {0x2, 0x7}, {0x5, 0x6}, {0x3, 0x5}, {0x6, 0x2}, {0x4, 0x5}, {0x0, 0x3}, {0x0, 0x6},
  {0x1, 0x4}, {0x2, 0x0}, {0x5, 0x0}, {0x3, 0x1}, {0x7, 0x2}, {0x6, 0x5}, {0x4, 0x3}, {0x0, 0x7},
  {0x1, 0x6}, {0x3, 0x4}, {0x6, 0x0}, {0x5, 0x1}, {0x3, 0x3}, {0x6, 0x6}, {0x5, 0x5}, {0x2, 0x3},
  {0x4, 0x6}, {0x1, 0x5}, {0x2, 0x2}, {0x4, 0x4}, {0x0, 0x1}, {0x1, 0x2}, {0x2, 0x4}, {0x4, 0x0}
};
const HBYTE KS = {0x0, 0x8};
void ti_ac(NIB4 *s, const u8 rn){
  s[0].n0  ^= KS.c0;
  s[0].n4  ^= KS.c0 ^ 1;
  s[0].n8  ^= KS.c1 ^ 2;
  s[0].n12 ^= KS.c1 ^ 3;

  s[0].n1  ^= RC[rn].c0;
  s[0].n5  ^= RC[rn].c1;
  s[0].n9  ^= RC[rn].c0;
  s[0].n13 ^= RC[rn].c1;
}

static void ti_ak(u64 *s, const u64 *k, const u8 p){
  s[0] ^= k[p*3  ];
  s[1] ^= k[p*3+1];
  s[2] ^= k[p*3+2];
}

void ti_encrypt(u64 *c, const u64 *m, const u64 *k){
  c[0] = m[0];
  c[1] = m[1];
  c[2] = m[2];

  u64 *s = c;
  u8 step, rn;
  for (step = 0; step < 12; step++){
	  ti_ak(s, k, step & 1);
    for (rn = 0; rn < 4; rn++){
      ti_ac((NIB4  *) s, step * 4 + rn);
      ti_sc((BIT64 *) s, ((step == 11) & (rn == 2)));
      ti_sr((NIB4  *) s, (NIB4 *) s);
      ti_mc((BIT64 *) s);
    }
  }
  ti_ak(s, k, step & 1);
}