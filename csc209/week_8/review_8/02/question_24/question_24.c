#include "readline.h"
#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 20

int main(void) {

    char *words[MAX_SIZE], ch, word[MAX_SIZE];

    while(true) {
        printf("Enter word:");
        // read word
        read_word(word);
        ch = getchar();
        printf("%c", ch);

        if (ch == '\n') {
            printf("I am here");
        }

        // store word
    }

    return 0;
}