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
    count += (ch >> 0) & 1;
    count += (ch >> 1) & 1;
    count += (ch >> 2) & 1;
    count += (ch >> 3) & 1;
    count += (ch >> 4) & 1;
    count += (ch >> 5) & 1;
    count += (ch >> 6) & 1;
    count += (ch >> 7) & 1;

    return count;
}
