#include <stdio.h>

#define MAX_VALUE 80

void encrypt(char *message, int shift);

int main(void) {

    char c, message[MAX_VALUE], *p;

    int shift;

    printf("Enter message to be encrypted: ");
    for (p = message; (c = getchar()) != '\n'; p++) {
        if (p == message + (MAX_VALUE-1)) {
            break;
        }
        *p = c;
    }

    *p = '\0';

    printf("Enter shift amount (1-25): ");
    scanf("%d", &shift);

    encrypt(message, shift);

    printf("Encrypted message: %s", &message);

    printf("\n");

    return 0;
}

void encrypt(char *message, int shift) {
    char *p;
    for (p = message; *p !=  '\0'; p++) {
        if (*p >= 'A' && *p <= 'Z')
            *p = ((*p - 'A') + shift) % 26 + 'A';
        else if (*p >= 'a' && *p <= 'z')
            *p = ((*p - 'a') + shift) % 26 + 'a';
    }
}