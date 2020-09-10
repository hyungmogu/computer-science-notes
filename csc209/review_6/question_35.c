#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

#define SIZE 100

bool is_palindrome(const char *message);

int main(void) {
    char c, message[SIZE], *p = message;

    printf("Enter a message: ");

    while ((c = getchar()) != '\n') {
        if (!isalpha(c)) {
            continue;
        }

        *p++ = tolower(c);
    }

    *p = '\0';

    // Check if characters in array is palindrome
    if (is_palindrome(message)) {
        printf("Palindrome");
    } else {
        printf("Not a Palindrome");
    }

    return 0;
}

bool is_palindrome(const char *message) {
    char const *p = message;
    char const *q = message;

    while(*q++)
        ;

    while (p < q) {
        if (*q == '\0') {
            q--;
            continue;
        }

        if (*p++ != *q--) {
            return false;
        }
    }

    return true;
}