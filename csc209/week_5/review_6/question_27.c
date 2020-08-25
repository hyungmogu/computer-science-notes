#include <stdio.h>
#include <ctype.h>

#define SIZE 100

int compute_vowel_count(const char *sentence);

int main(void) {

    char ch, sentence[SIZE], *p = sentence;
    int vowels;

    printf("Enter a sentence: ");
    while ((ch = getchar()) != EOF) {
        if (ch == '\n') {
            break;
        }

        *p++ = ch;
    }

    vowels = compute_vowel_count(sentence);

    printf("Your sentence contains %d vowels.\n", vowels);
    return 0;
}

int compute_vowel_count(const char *sentence) {
    int count = 0;

    do {
        switch (toupper(*sentence)) {
            case 'A': case 'E': case 'I': case 'O': case 'U':
                count++;
                break;
            default:
                break;
        }
    } while (*sentence++);

    return count;
}