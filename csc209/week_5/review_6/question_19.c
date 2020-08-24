#include <stdio.h>

int main(void) {
    int n = 20;
    char smallest_word[n+1], largest_word[n+1], s[n+1];


    do {
        printf("Enter word: ");
        scanf("%s", s); // ask user to enter words
        printf("\n");

        if (strcmp(s, smallest_word) < 0) {
            strcpy(smallest_word, s);
            *smallest_word = '\0';
            printf("%s", smallest_word);
        }

    } while (strlen(s) != 4); // stop program when user enters four letter words

    return 0;
}
