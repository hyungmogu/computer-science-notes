#include <stdio.h>
#include <stdlib.h>

int rotate_left(int hex, int n);
int rotate_right(int hex, int n);

int main() {
    printf("rotated left: %x", rotate_left(0x12345678, 4));
    printf("rotated left: %x", rotate_right(0x12345678, 4));
    return 0;
}

int rotate_left(int hex, int n) {
    int res = hex;

    for (int i = 0; i < n; i++) {
        res = (res >> 4) | (res << 28);
    }

    return res;
}

int rotate_right(int hex, int n) {
    int res = hex;

    for (int i = 0; i < n; i++) {
        res = (res << 4) | (res >> 28);
    }

    return res;
}