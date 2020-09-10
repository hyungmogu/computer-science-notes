#include <stdio.h>

#define SIZE 100

double compute_average_word_length(const char *sentence);

int main(void) {

    char sentence[SIZE], *p, c;
    double length = 0.0;

    printf("Enter a sentence: ");
    for (p = sentence; (c = getchar()) != '\n'; p++) {
        *p = c;
    }

    *p = '\0';

    length = compute_average_word_length(sentence);
    printf("Average word length: %.2f\n", length);
    return 0;
}

double compute_average_word_length(const char *sentence) {
    int words = 0, length = 0;

    for (; *sentence != '\0'; sentence++) {
        if (*sentence == ' ')
            words++;
        else
            length++;
    }

    if (length > 0 && *sentence == '\0') {
        words++;
    }

    return (double)length/words;
}