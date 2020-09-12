#include <stdio.h>
#include <stdlib.h>

int count_ones(unsigned char ch);

int main() {
    printf("%x\n", '1');
    printf("%d\n", count_ones('1'));
    return 0;
}

int count_ones (unsigned char ch)
{
    int count = 0;
    for (int i = 0; i < 8; i++) {
        count += (ch >> i) & 1;
    }

    return count;
}
