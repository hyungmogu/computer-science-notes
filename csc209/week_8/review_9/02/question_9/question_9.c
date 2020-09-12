#include <stdio.h>
#include <stdlib.h>

int count_ones(unsigned char ch);

int main() {
    return 0;
}

int count_ones (unsigned char ch)
{
    int count = 0;
    for (int i = 0; i < sizeof(unsigned char); i++) {
        if ((ch >> i) & 1) {
            count += 1;
        }
    }
}
