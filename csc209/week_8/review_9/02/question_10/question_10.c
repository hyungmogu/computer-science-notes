#include <stdio.h>
#include <stdlib.h>

int reverse_bits(unsigned int n);

int main() {
    printf("%d", reverse_bits(100));
    return 0;
}

int reverse_bits(unsigned int n)
{
    int max_bits = (sizeof(int) * 4);
    unsigned int bits[max_bits], res = 0;

    for (int i = 0; i < max_bits; i++) {
        bits[i] = (n >> i) & 1;
    }

    for (int i = max_bits - 1; i >= 0; i--) {
        res |= bits[(max_bits - 1) - i] << i;
    }

    return res;
}
