#include <stdio.h>
#include <stdlib.h>

unsigned short swap_bytes(unsigned short i);

int main() {
    unsigned short i;
    printf("Enter a hexadecimal number (up to four digits):");
    scanf("%hx", &i);

    i = swap_bytes(i);

    printf("Number with bytes swapped: %hx", i);
    return 0;
}

unsigned short swap_bytes(unsigned short i) {
    unsigned short i1,i2,i3,i4, res;

    i1 = i & 255;
    i2 = (i >> 8) & 255;

    res = (i1 << 8) | i2;

    return res;
}