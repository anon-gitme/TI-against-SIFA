#include "config.h"

// TI computation for 0-th element
void G_0_b3(BIT64 *y, const BIT64 *x);
void G_0_b2(BIT64 *y, const BIT64 *x);
void G_0_b1(BIT64 *y, const BIT64 *x);
void G_0_b0(BIT64 *y, const BIT64 *x, u8 is_faulted);
void F_0_b3(BIT64 *a, const BIT64 *y);
void F_0_b2(BIT64 *a, const BIT64 *y);
void F_0_b1(BIT64 *a, const BIT64 *y);
void F_0_b0(BIT64 *a, const BIT64 *y);

// TI computation for 1-th element
void G_1_b3(BIT64 *y, const BIT64 *x);
void G_1_b2(BIT64 *y, const BIT64 *x);
void G_1_b1(BIT64 *y, const BIT64 *x);
void G_1_b0(BIT64 *y, const BIT64 *x);
void F_1_b3(BIT64 *a, const BIT64 *y);
void F_1_b2(BIT64 *a, const BIT64 *y);
void F_1_b1(BIT64 *a, const BIT64 *y);
void F_1_b0(BIT64 *a, const BIT64 *y);

// TI computation for 2-th element
void G_2_b3(BIT64 *y, const BIT64 *x);
void G_2_b2(BIT64 *y, const BIT64 *x);
void G_2_b1(BIT64 *y, const BIT64 *x);
void G_2_b0(BIT64 *y, const BIT64 *x);
void F_2_b3(BIT64 *a, const BIT64 *y);
void F_2_b2(BIT64 *a, const BIT64 *y);
void F_2_b1(BIT64 *a, const BIT64 *y);
void F_2_b0(BIT64 *a, const BIT64 *y);

// TI computation for 3-th element
void G_3_b3(BIT64 *y, const BIT64 *x);
void G_3_b2(BIT64 *y, const BIT64 *x);
void G_3_b1(BIT64 *y, const BIT64 *x);
void G_3_b0(BIT64 *y, const BIT64 *x);
void F_3_b3(BIT64 *a, const BIT64 *y);
void F_3_b2(BIT64 *a, const BIT64 *y);
void F_3_b1(BIT64 *a, const BIT64 *y);
void F_3_b0(BIT64 *a, const BIT64 *y);

// TI computation for 4-th element
void G_4_b3(BIT64 *y, const BIT64 *x);
void G_4_b2(BIT64 *y, const BIT64 *x);
void G_4_b1(BIT64 *y, const BIT64 *x);
void G_4_b0(BIT64 *y, const BIT64 *x);
void F_4_b3(BIT64 *a, const BIT64 *y);
void F_4_b2(BIT64 *a, const BIT64 *y);
void F_4_b1(BIT64 *a, const BIT64 *y);
void F_4_b0(BIT64 *a, const BIT64 *y);

// TI computation for 5-th element
void G_5_b3(BIT64 *y, const BIT64 *x);
void G_5_b2(BIT64 *y, const BIT64 *x);
void G_5_b1(BIT64 *y, const BIT64 *x);
void G_5_b0(BIT64 *y, const BIT64 *x);
void F_5_b3(BIT64 *a, const BIT64 *y);
void F_5_b2(BIT64 *a, const BIT64 *y);
void F_5_b1(BIT64 *a, const BIT64 *y);
void F_5_b0(BIT64 *a, const BIT64 *y);

// TI computation for 6-th element
void G_6_b3(BIT64 *y, const BIT64 *x);
void G_6_b2(BIT64 *y, const BIT64 *x);
void G_6_b1(BIT64 *y, const BIT64 *x);
void G_6_b0(BIT64 *y, const BIT64 *x);
void F_6_b3(BIT64 *a, const BIT64 *y);
void F_6_b2(BIT64 *a, const BIT64 *y);
void F_6_b1(BIT64 *a, const BIT64 *y);
void F_6_b0(BIT64 *a, const BIT64 *y);

// TI computation for 7-th element
void G_7_b3(BIT64 *y, const BIT64 *x);
void G_7_b2(BIT64 *y, const BIT64 *x);
void G_7_b1(BIT64 *y, const BIT64 *x);
void G_7_b0(BIT64 *y, const BIT64 *x);
void F_7_b3(BIT64 *a, const BIT64 *y);
void F_7_b2(BIT64 *a, const BIT64 *y);
void F_7_b1(BIT64 *a, const BIT64 *y);
void F_7_b0(BIT64 *a, const BIT64 *y);

// TI computation for 8-th element
void G_8_b3(BIT64 *y, const BIT64 *x);
void G_8_b2(BIT64 *y, const BIT64 *x);
void G_8_b1(BIT64 *y, const BIT64 *x);
void G_8_b0(BIT64 *y, const BIT64 *x);
void F_8_b3(BIT64 *a, const BIT64 *y);
void F_8_b2(BIT64 *a, const BIT64 *y);
void F_8_b1(BIT64 *a, const BIT64 *y);
void F_8_b0(BIT64 *a, const BIT64 *y);

// TI computation for 9-th element
void G_9_b3(BIT64 *y, const BIT64 *x);
void G_9_b2(BIT64 *y, const BIT64 *x);
void G_9_b1(BIT64 *y, const BIT64 *x);
void G_9_b0(BIT64 *y, const BIT64 *x);
void F_9_b3(BIT64 *a, const BIT64 *y);
void F_9_b2(BIT64 *a, const BIT64 *y);
void F_9_b1(BIT64 *a, const BIT64 *y);
void F_9_b0(BIT64 *a, const BIT64 *y);

// TI computation for 10-th element
void G_10_b3(BIT64 *y, const BIT64 *x);
void G_10_b2(BIT64 *y, const BIT64 *x);
void G_10_b1(BIT64 *y, const BIT64 *x);
void G_10_b0(BIT64 *y, const BIT64 *x);
void F_10_b3(BIT64 *a, const BIT64 *y);
void F_10_b2(BIT64 *a, const BIT64 *y);
void F_10_b1(BIT64 *a, const BIT64 *y);
void F_10_b0(BIT64 *a, const BIT64 *y);

// TI computation for 11-th element
void G_11_b3(BIT64 *y, const BIT64 *x);
void G_11_b2(BIT64 *y, const BIT64 *x);
void G_11_b1(BIT64 *y, const BIT64 *x);
void G_11_b0(BIT64 *y, const BIT64 *x);
void F_11_b3(BIT64 *a, const BIT64 *y);
void F_11_b2(BIT64 *a, const BIT64 *y);
void F_11_b1(BIT64 *a, const BIT64 *y);
void F_11_b0(BIT64 *a, const BIT64 *y);

// TI computation for 12-th element
void G_12_b3(BIT64 *y, const BIT64 *x);
void G_12_b2(BIT64 *y, const BIT64 *x);
void G_12_b1(BIT64 *y, const BIT64 *x);
void G_12_b0(BIT64 *y, const BIT64 *x);
void F_12_b3(BIT64 *a, const BIT64 *y);
void F_12_b2(BIT64 *a, const BIT64 *y);
void F_12_b1(BIT64 *a, const BIT64 *y);
void F_12_b0(BIT64 *a, const BIT64 *y);

// TI computation for 13-th element
void G_13_b3(BIT64 *y, const BIT64 *x);
void G_13_b2(BIT64 *y, const BIT64 *x);
void G_13_b1(BIT64 *y, const BIT64 *x);
void G_13_b0(BIT64 *y, const BIT64 *x);
void F_13_b3(BIT64 *a, const BIT64 *y);
void F_13_b2(BIT64 *a, const BIT64 *y);
void F_13_b1(BIT64 *a, const BIT64 *y);
void F_13_b0(BIT64 *a, const BIT64 *y);

// TI computation for 14-th element
void G_14_b3(BIT64 *y, const BIT64 *x);
void G_14_b2(BIT64 *y, const BIT64 *x);
void G_14_b1(BIT64 *y, const BIT64 *x);
void G_14_b0(BIT64 *y, const BIT64 *x);
void F_14_b3(BIT64 *a, const BIT64 *y);
void F_14_b2(BIT64 *a, const BIT64 *y);
void F_14_b1(BIT64 *a, const BIT64 *y);
void F_14_b0(BIT64 *a, const BIT64 *y);

// TI computation for 15-th element
void G_15_b3(BIT64 *y, const BIT64 *x);
void G_15_b2(BIT64 *y, const BIT64 *x);
void G_15_b1(BIT64 *y, const BIT64 *x);
void G_15_b0(BIT64 *y, const BIT64 *x);
void F_15_b3(BIT64 *a, const BIT64 *y);
void F_15_b2(BIT64 *a, const BIT64 *y);
void F_15_b1(BIT64 *a, const BIT64 *y);
void F_15_b0(BIT64 *a, const BIT64 *y);

