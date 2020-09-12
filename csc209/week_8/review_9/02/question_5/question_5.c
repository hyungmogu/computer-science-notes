#include <stdio.h>
#include <stdlib.h>

#define GET_RED(color) (int)(color & 255)
#define GET_GREEN(color) (int)((color >> 8) & 255)
#define GET_BLUE(color) (int)((color >> 16) & 255)

int main() {
    printf("%x\n", GET_RED(0xfff8f9));
    printf("%x\n", GET_GREEN(0xfff8f9));
    printf("%x\n", GET_BLUE(0xfff8f9));

    return 0;
}