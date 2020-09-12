#include <stdio.h>
#include <stdlib.h>

int main() {
    unsigned short i;
    printf("Enter a hexadecimal number (up to four digits):");
    scanf("%hx", &i);

    i = swap_bytes(i);

    printf("Number with bytes swapped: %d", i);
    return 0;
}