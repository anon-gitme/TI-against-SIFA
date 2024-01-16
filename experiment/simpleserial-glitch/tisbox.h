#include "config.h"

// TI computation for 0-th element
void G_0_0(BIT64 *y, const BIT64 *x, const u8 is_faulted);
void G_0_1(BIT64 *y, const BIT64 *x);
void G_0_2(BIT64 *y, const BIT64 *x);
void F_0_0(BIT64 *a, const BIT64 *y);
void F_0_1(BIT64 *a, const BIT64 *y);
void F_0_2(BIT64 *a, const BIT64 *y);

// TI computation for 1-th element
void G_1_0(BIT64 *y, const BIT64 *x);
void G_1_1(BIT64 *y, const BIT64 *x);
void G_1_2(BIT64 *y, const BIT64 *x);
void F_1_0(BIT64 *a, const BIT64 *y);
void F_1_1(BIT64 *a, const BIT64 *y);
void F_1_2(BIT64 *a, const BIT64 *y);

// TI computation for 2-th element
void G_2_0(BIT64 *y, const BIT64 *x);
void G_2_1(BIT64 *y, const BIT64 *x);
void G_2_2(BIT64 *y, const BIT64 *x);
void F_2_0(BIT64 *a, const BIT64 *y);
void F_2_1(BIT64 *a, const BIT64 *y);
void F_2_2(BIT64 *a, const BIT64 *y);

// TI computation for 3-th element
void G_3_0(BIT64 *y, const BIT64 *x);
void G_3_1(BIT64 *y, const BIT64 *x);
void G_3_2(BIT64 *y, const BIT64 *x);
void F_3_0(BIT64 *a, const BIT64 *y);
void F_3_1(BIT64 *a, const BIT64 *y);
void F_3_2(BIT64 *a, const BIT64 *y);

// TI computation for 4-th element
void G_4_0(BIT64 *y, const BIT64 *x);
void G_4_1(BIT64 *y, const BIT64 *x);
void G_4_2(BIT64 *y, const BIT64 *x);
void F_4_0(BIT64 *a, const BIT64 *y);
void F_4_1(BIT64 *a, const BIT64 *y);
void F_4_2(BIT64 *a, const BIT64 *y);

// TI computation for 5-th element
void G_5_0(BIT64 *y, const BIT64 *x);
void G_5_1(BIT64 *y, const BIT64 *x);
void G_5_2(BIT64 *y, const BIT64 *x);
void F_5_0(BIT64 *a, const BIT64 *y);
void F_5_1(BIT64 *a, const BIT64 *y);
void F_5_2(BIT64 *a, const BIT64 *y);

// TI computation for 6-th element
void G_6_0(BIT64 *y, const BIT64 *x);
void G_6_1(BIT64 *y, const BIT64 *x);
void G_6_2(BIT64 *y, const BIT64 *x);
void F_6_0(BIT64 *a, const BIT64 *y);
void F_6_1(BIT64 *a, const BIT64 *y);
void F_6_2(BIT64 *a, const BIT64 *y);

// TI computation for 7-th element
void G_7_0(BIT64 *y, const BIT64 *x);
void G_7_1(BIT64 *y, const BIT64 *x);
void G_7_2(BIT64 *y, const BIT64 *x);
void F_7_0(BIT64 *a, const BIT64 *y);
void F_7_1(BIT64 *a, const BIT64 *y);
void F_7_2(BIT64 *a, const BIT64 *y);

// TI computation for 8-th element
void G_8_0(BIT64 *y, const BIT64 *x);
void G_8_1(BIT64 *y, const BIT64 *x);
void G_8_2(BIT64 *y, const BIT64 *x);
void F_8_0(BIT64 *a, const BIT64 *y);
void F_8_1(BIT64 *a, const BIT64 *y);
void F_8_2(BIT64 *a, const BIT64 *y);

// TI computation for 9-th element
void G_9_0(BIT64 *y, const BIT64 *x);
void G_9_1(BIT64 *y, const BIT64 *x);
void G_9_2(BIT64 *y, const BIT64 *x);
void F_9_0(BIT64 *a, const BIT64 *y);
void F_9_1(BIT64 *a, const BIT64 *y);
void F_9_2(BIT64 *a, const BIT64 *y);

// TI computation for 10-th element
void G_10_0(BIT64 *y, const BIT64 *x);
void G_10_1(BIT64 *y, const BIT64 *x);
void G_10_2(BIT64 *y, const BIT64 *x);
void F_10_0(BIT64 *a, const BIT64 *y);
void F_10_1(BIT64 *a, const BIT64 *y);
void F_10_2(BIT64 *a, const BIT64 *y);

// TI computation for 11-th element
void G_11_0(BIT64 *y, const BIT64 *x);
void G_11_1(BIT64 *y, const BIT64 *x);
void G_11_2(BIT64 *y, const BIT64 *x);
void F_11_0(BIT64 *a, const BIT64 *y);
void F_11_1(BIT64 *a, const BIT64 *y);
void F_11_2(BIT64 *a, const BIT64 *y);

// TI computation for 12-th element
void G_12_0(BIT64 *y, const BIT64 *x);
void G_12_1(BIT64 *y, const BIT64 *x);
void G_12_2(BIT64 *y, const BIT64 *x);
void F_12_0(BIT64 *a, const BIT64 *y);
void F_12_1(BIT64 *a, const BIT64 *y);
void F_12_2(BIT64 *a, const BIT64 *y);

// TI computation for 13-th element
void G_13_0(BIT64 *y, const BIT64 *x);
void G_13_1(BIT64 *y, const BIT64 *x);
void G_13_2(BIT64 *y, const BIT64 *x);
void F_13_0(BIT64 *a, const BIT64 *y);
void F_13_1(BIT64 *a, const BIT64 *y);
void F_13_2(BIT64 *a, const BIT64 *y);

// TI computation for 14-th element
void G_14_0(BIT64 *y, const BIT64 *x);
void G_14_1(BIT64 *y, const BIT64 *x);
void G_14_2(BIT64 *y, const BIT64 *x);
void F_14_0(BIT64 *a, const BIT64 *y);
void F_14_1(BIT64 *a, const BIT64 *y);
void F_14_2(BIT64 *a, const BIT64 *y);

// TI computation for 15-th element
void G_15_0(BIT64 *y, const BIT64 *x);
void G_15_1(BIT64 *y, const BIT64 *x);
void G_15_2(BIT64 *y, const BIT64 *x);
void F_15_0(BIT64 *a, const BIT64 *y);
void F_15_1(BIT64 *a, const BIT64 *y);
void F_15_2(BIT64 *a, const BIT64 *y);