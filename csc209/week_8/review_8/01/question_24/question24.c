#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "readline.h"

#define MAX_LENGTH 20

struct node {
    char name[MAX_LENGTH];
};

int compare_parts(const void *p, const void *q);

int main(void) {
    int arr_size = 10, n, word_length;
    struct node *words, *p;

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
        // scan for word
        printf("Enter Word: ");
        // read and store each word
        word_length = read_line(words[n].name, MAX_LENGTH);

        if(word_length == 0) {
            break;
        }
    }

    qsort(words, n, sizeof(words[0]), compare_parts);

    printf("In sorted order: ");
    for (int i = 0; i < n; i++)
    {
        printf("%s", (words[i]).name);

        if (i != n-1) {
            putchar(' ');
        }
    }

    printf("\n");

    free(words);

    return 0;
}

int compare_parts(const void *p, const void *q) {
    const struct node *p1 = p;
    const struct node *q1 = q;

    return strcmp((*p1).name, (*q1).name);
}