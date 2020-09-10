#include <stdio.h>

int main() {
    char text[20];
    text[0] = 'h';
    text[1] = 'e';
    text[2] = 'l';
    text[3] = 'l';
    text[4] = 'o';

    int i;
    for (i = 0; i < 20; i++) {
        printf("%c", text[i]);
    }

    printf("\n");

    return 0;
}