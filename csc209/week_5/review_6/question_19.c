#include <stdio.h>
#include <string.h>

int main(void) {
    int n = 20;
    char smallest_word[n+1], largest_word[n+1], s[n+1];

    smallest_word[0] = '\0';
    largest_word[0] = '\0';


    do {
        printf("Enter word: ");
        scanf("%s", s);

        if (largest_word[0] == '\0') {
            strcpy(largest_word, s);
            printf("%s\n", s);
        }

        if (smallest_word[0] == '\0') {
            strcpy(smallest_word, s);
            printf("%s\n", s);
        }

        if (strcmp(s, largest_word) > 0) {
            strcpy(largest_word, s);
        } else if (strcmp(s, smallest_word) < 0) {
            strcpy(smallest_word, s);
        }

    } while (strlen(s) != 4);


    printf("Smallest word: %s\n", smallest_word);
    printf("Largest word: %s\n", largest_word);

    return 0;
}
