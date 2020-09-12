#include "readline.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_SIZE 21

void read_word(char word[]);

int main(void) {
    int max_words = 10, num_words, i, j;
    char **words, ch, word[MAX_SIZE];

    words = malloc(max_words * (sizeof(char *) * MAX_SIZE));

    for(i = 0, num_words = 0; ; num_words = i + 1, i++) {
        if (num_words == max_words) {
            words = realloc(words, max_words * 2);
            max_words *= 2;
        }

        printf("Enter word:");
        read_word(word);

        // exit word if the registered char is newline
        if (word[0] == '\n') {
            break;
        } else {
            // store word
            words[i] = malloc(strlen(word) + 1);
            strcpy(words[i], word);
        }
    }

    // sort words
    for (j = 0; j < num_words; j++) {

    }


    // display words


    // free memory

    return 0;
}

void read_word(char word[]) {
    char ch;
    int i = 0;

    // 1  if received char is a space, then continue
    // 2. if first char of read_word is \n, then add to word and exit
    // 3. if first char of read_word is not \n, then add to word
    // 4. at the end, add '\0'

    while(true) {
        ch = getchar();

        if (ch == ' ') {
            continue;
        }

        word[i++] = ch;

        if (ch == '\n') {
            word[i] = '\0';
            break;
        }
    }
}