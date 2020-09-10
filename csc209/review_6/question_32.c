#include <stdio.h>
#include <stdbool.h> // bool
#include <ctype.h> /* toupper, isalpha */

#define SIZE 50

bool are_anagrams(const char *word1, const char *word2);

int main(void) {

    char c, word1[SIZE], word2[SIZE],
         *pa = word1, *pb = word2;


    printf("Enter first word: ");
    while ((c = getchar()) != '\n') {
        if (isalpha(c)) {
            *pa++ = c;
        }
    }

    *pa = '\0';

    printf("Enter second word: ");
    while ((c = getchar()) != '\n') {
        if (isalpha(c)) {
            *pb++ = c;
        }
    }

    *pb = '\0';


    if (are_anagrams(word1, word2)) {
        printf("The words are anagrams.\n");
    } else {
        printf("The words are not anagrams.\n");
    }

    return 0;
}

bool are_anagrams(const char *word1, const char *word2) {
    int letters[26] = {0}, *p;

    while (*word1 != '\0') {
        letters[toupper(*word1) - 'A']++;
        word1++;
    }

    while (*word2 != '\0') {
        letters[toupper(*word2) - 'A']--;
        word2++;
    }

    for (p = letters; p < letters + 26; p++) {
        if (*p != 0) {
            return false;
        }
    }

    return true;
}