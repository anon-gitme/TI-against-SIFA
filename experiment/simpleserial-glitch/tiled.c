#include "tisbox.h"
#include "timixcol.h"
#include "tiled.h"
// #include "utils.h"


static void ti_sc(BIT64 *s, u8 is_faulted){
  BIT64 y[3];

  // TI computation for 0-th element
  G_0_0(y, s, is_faulted);
  G_0_1(y, s);
  G_0_2(y, s);
  F_0_0(s, y);
  F_0_1(s, y);
  F_0_2(s, y);

  // TI computation for 1-th element
  G_1_0(y, s);
  G_1_1(y, s);
  G_1_2(y, s);
  F_1_0(s, y);
  F_1_1(s, y);
  F_1_2(s, y);

  // TI computation for 2-th element
  G_2_0(y, s);
  G_2_1(y, s);
  G_2_2(y, s);
  F_2_0(s, y);
  F_2_1(s, y);
  F_2_2(s, y);

  // TI computation for 3-th element
  G_3_0(y, s);
  G_3_1(y, s);
  G_3_2(y, s);
  F_3_0(s, y);
  F_3_1(s, y);
  F_3_2(s, y);

  // TI computation for 4-th element
  G_4_0(y, s);
  G_4_1(y, s);
  G_4_2(y, s);
  F_4_0(s, y);
  F_4_1(s, y);
  F_4_2(s, y);

  // TI computation for 5-th element
  G_5_0(y, s);
  G_5_1(y, s);
  G_5_2(y, s);
  F_5_0(s, y);
  F_5_1(s, y);
  F_5_2(s, y);

  // TI computation for 6-th element
  G_6_0(y, s);
  G_6_1(y, s);
  G_6_2(y, s);
  F_6_0(s, y);
  F_6_1(s, y);
  F_6_2(s, y);

  // TI computation for 7-th element
  G_7_0(y, s);
  G_7_1(y, s);
  G_7_2(y, s);
  F_7_0(s, y);
  F_7_1(s, y);
  F_7_2(s, y);

  // TI computation for 8-th element
  G_8_0(y, s);
  G_8_1(y, s);
  G_8_2(y, s);
  F_8_0(s, y);
  F_8_1(s, y);
  F_8_2(s, y);

  // TI computation for 9-th element
  G_9_0(y, s);
  G_9_1(y, s);
  G_9_2(y, s);
  F_9_0(s, y);
  F_9_1(s, y);
  F_9_2(s, y);

  // TI computation for 10-th element
  G_10_0(y, s);
  G_10_1(y, s);
  G_10_2(y, s);
  F_10_0(s, y);
  F_10_1(s, y);
  F_10_2(s, y);

  // TI computation for 11-th element
  G_11_0(y, s);
  G_11_1(y, s);
  G_11_2(y, s);
  F_11_0(s, y);
  F_11_1(s, y);
  F_11_2(s, y);

  // TI computation for 12-th element
  G_12_0(y, s);
  G_12_1(y, s);
  G_12_2(y, s);
  F_12_0(s, y);
  F_12_1(s, y);
  F_12_2(s, y);

  // TI computation for 13-th element
  G_13_0(y, s);
  G_13_1(y, s);
  G_13_2(y, s);
  F_13_0(s, y);
  F_13_1(s, y);
  F_13_2(s, y);

  // TI computation for 14-th element
  G_14_0(y, s);
  G_14_1(y, s);
  G_14_2(y, s);
  F_14_0(s, y);
  F_14_1(s, y);
  F_14_2(s, y);

  // TI computation for 15-th element
  G_15_0(y, s);
  G_15_1(y, s);
  G_15_2(y, s);
  F_15_0(s, y);
  F_15_1(s, y);
  F_15_2(s, y);
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
      ti_sc((BIT64 *) s, ((step == 11) & (rn == 3)));
      ti_sr((NIB4  *) s, (NIB4 *) s);
      ti_mc((BIT64 *) s);
    }
  }
  ti_ak(s, k, step & 1);
}