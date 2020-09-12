#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_SIZE 21

void read_word(char word[]);
int compare_parts(const void *p, const void *q);

int main(void) {
    int max_words = 10, num_words, i, k, l;
    char **words, ch, word[MAX_SIZE];

    words = malloc(max_words * (sizeof(char *) * MAX_SIZE));

    if (words == NULL) {
        printf("No space left");
        exit(1);
    }

    for(i = 0, num_words = 0; ; i++, num_words++) {
        if (num_words == max_words) {
            words = realloc(words, max_words * 2);
            max_words *= 2;
        }

        printf("Enter word:");
        read_word(word);

        // exit word if the registered char is newline
        if (word[0] == '\0') {
            break;
        } else {
            // store word
            words[i] = malloc(sizeof(char) * MAX_SIZE);
            if (words[i] == NULL) {
                printf("No space left");
                exit(1);
            }
            strcpy(words[i], word);
        }
    }

    // sort words
    if (num_words > 0) {
        qsort(words, num_words, sizeof(words[0]), compare_parts);
    }

    // display words
    for (k = 0; k < num_words; k++) {
        printf("%s", words[k]);
        if (k != num_words - 1) {
            putchar(' ');
        }
    }

    printf("\n");

    // free memory
    for(l = 0; l < num_words; l++) {
        free(words[l]);
    }

    free(words);

    return 0;
}

int compare_parts(const void *p,const void *q) {

    return strcmp(*(char **)p, *(char **)q);
}

void read_word(char word[]) {
    char ch;
    int i = 0;

    while(true) {
        ch = getchar();

        if (ch == ' ') {
            continue;
        }

        if (ch == '\n') {
            word[i] = '\0';
            break;
        }

        word[i] = ch;
        i++;
    }
}