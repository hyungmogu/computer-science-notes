#include <stdio.h>

#define MAX_VALUE 80

void encrypt(char *message, int shift);

int main(void) {

    char c, sentence[MAX_VALUE] = {0};

    int i, shift, length;

    printf("Enter message to be encrypted: ");
    for (i = 0, length = 0; (c = getchar()) != '\n' && i < MAX_VALUE; i++) {
        length++;
        sentence[i] = c;
    }

    printf("Enter shift amount (1-25): ");
    scanf("%d", &shift);

    printf("Encrypted message: %s", encrypt(message, shift));

    printf("\n");

    return 0;
}

void encrypt(char *message, int shift) {
    for (i = 0; i < length; i++) {
        if (message[i] >= 'A' && message[i] <= 'Z')
            message[i] = ((message[i] - 'A') + shift) % 26 + 'A';
        else if (sentence[i] >= 'a' && message[i] <= 'z')
            message[i] = ((message[i] - 'a') + shift) % 26 + 'a';

        putchar(message[i]);
    }
}