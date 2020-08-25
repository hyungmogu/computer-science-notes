#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

#define SIZE 100

bool is_palindrome(const char *message);

int main(void) {
    char c, array[SIZE],
            *p = array,
            *q = array;

    // Read characters
    // Put characters into array
    printf("Enter a message: ");

    do {
        c = getchar();

        if (c == '\n') {
            break;
        }

        if (!isalpha(c)) {
            continue;
        }

        *q++ = tolower(c);
    } while (q < array + SIZE);
    // Set pointer to last element in the array
    q--;
    // Check if characters in array is palindrome
    if (is_palindrome(p,q)) {
        printf("Palindrome");
    } else {
        printf("Not a Palindrome");
    }

    return 0;
}

bool is_palindrome(const char *message) {
    char *p, *q;

    while (p < q) {
        if (*p++ != *q--) {
            return false;
        }
    }

    return true;
}