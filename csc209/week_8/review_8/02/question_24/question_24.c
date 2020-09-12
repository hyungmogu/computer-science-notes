#include "readline.h"
#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 21

void read_word(char word[]);

int main(void) {
    int max_words = 10;
    char *words, ch, word[MAX_SIZE];

    words = malloc(sizeof(word[MAX_SIZE]) * max_words);

    while(true) {
        printf("Enter word:");
        // read word
        read_word(word);

        // exit word if the registered char is newline
        if (word[0] == '\0') {
            break;
        }

        // store word
    }

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