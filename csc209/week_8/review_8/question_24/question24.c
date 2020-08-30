#include <stdio.h>
#include <stdlib.h>
#include "readline.h"

#define MAX_LENGTH 20

struct node {
    char name[MAX_LENGTH];
};

int main(void) {
    int arr_size = 10, n, word_length;
    struct node *words;

    // create dynamically allocated array
    words = malloc(arr_size * sizeof(struct node));

    if (words == NULL) {
        printf("ERROR: Memory failed to allocate for words");
    }

    for(n = 0;;n++) {
        // double the size of array if at capacity
        if (n == arr_size) {
            arr_size *= 2;
            words = realloc(words, arr_size * sizeof(words[0]));
        }

        // read and store each word
        word_length = read_line((words[n])->name, MAX_LENGTH);

        if(word_length == 0) {
            break;
        }
    }

    // sort_words(struct node words[], int n);

    // printf("In sorted order");
    // print_words(struct node words[], int n);

    return 0;
}