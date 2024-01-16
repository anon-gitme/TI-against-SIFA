/*
    This file is part of the ChipWhisperer Example Targets
    Copyright (C) 2012-2020 NewAE Technology Inc.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include "hal.h"
#include <stdint.h>
#include <stdlib.h>

#include "simpleserial.h"
#include "vu_tiled.h"
#include "utils.h"


u8 glitch_ti_encrypt(u8 cmd, u8 scmd, u8 len, u8* in){
    u64 m;
    u64 k[2];

    u8_to_u64(&m , in   );
    u8_to_u64(k  , in+8 );
    u8_to_u64(k+1, in+16);

    u64 sh_m[3];
    u64 sh_k[6];
    u64 sh_c[3];
    sh_encode(sh_m, m);
    sh_key_encode(sh_k, k);
    ti_encrypt(sh_c, sh_m, sh_k);

    u64 c = sh_decode(sh_c);
    u8 out[8];
    u64_to_u8(out, c);

    simpleserial_put('r', 8, (u8*) &out);
    return 0x00;
}

// #pragma GCC pop_options

int main(void)
{
    platform_init();
    init_uart();
    trigger_setup();

    /* Device reset detected */
    putch('r');
    putch('R');
    putch('E');
    putch('S');
    putch('E');
    putch('T');
    putch(' ');
    putch(' ');
    putch(' ');
    putch('\n');

    simpleserial_init();
    // simpleserial_addcmd('g', 0, glitch_loop);
    // simpleserial_addcmd('c', 1, glitch_comparison);
    // #if SS_VER == SS_VER_2_1
    simpleserial_addcmd(0x01, 24, glitch_ti_encrypt); 
    // #else
    // simpleserial_addcmd('p', 5, password);
    // #endif
    // simpleserial_addcmd('i', 0, infinite_loop);
    while(1)
        simpleserial_get();
}
