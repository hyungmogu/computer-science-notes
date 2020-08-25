#include <stdio.h>
#include <stdbool.h> // bool
#include <ctype.h> /* toupper, isalpha */

#define SIZE 50

bool are_anagrams(const char *word1, const char *word2);

int main(void) {

    char c, word1[SIZE], word2[SIZE];

    printf("Enter first word: ");
    while ((c = getchar()) != '\n') {
        if (isalpha(c))

            letters[toupper(c) - 'A']++;
    }
    printf("Enter second word: ");
    while ((c = getchar()) != '\n') {
        if (isalpha(c))
            letters[toupper(c) - 'A']--;
    }

    for (i = 0; i < 26; i++) {
        if (letters[i] != 0) {
            same = 0;
            break;
        }
    }
    if (are_anagram(word1, word2)) {
        printf("The words are anagrams.\n");
        return 0;
    }
    printf("The words are not anagrams.\n");
    return 0;
}

bool are_anagrams(const char *word1, const char *word2) {

}