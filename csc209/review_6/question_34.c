#include <stdio.h>

#define SIZE 50

void reverse(char *message);

int main(void) {

    char message[SIZE], c, *p;

    p = &message[0];

    printf("Enter a message: ");

    // fill array
    while ((c = getchar()) != '\n') {
        *p++ = c;
    }

    *p = '\0';

    // reverse characters in array
    reverse(message);

    printf("Reversal is: %s", message);

    return 0;
}

void reverse (char *message) {
    char *q = message, *r = message, temp;

    while (*r++)
        ;

    while (q < r) {
        if (*r == '\0') {
            r--;
            continue;
        }

        temp = *q;
        *q++ = *r;
        *r-- = temp;
    }
}