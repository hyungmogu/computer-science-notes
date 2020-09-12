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
    unsigned short res;

    res = (i >> 8) | (i << 8);

    return res;
}