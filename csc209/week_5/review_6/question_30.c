#include <stdio.h>

#define MAX_VALUE 100
#define MAX_WORDS 30
#define MAX_SIZE 20

int main(void) {

    char sentence[MAX_WORDS][MAX_SIZE], c,
         terminating_char, **p = *sentence;

    int i = 0;

    printf("Enter a sentence: ");
    while((c = getchar()) != '\n') {
        if (c == '.' || c == '!' || c == '?') {
            terminating_char = c;
            p++;
            break;
        } else if (c == ' ') {
            **p='\0';
            p++;
        } else {
            **p++ = c;
        }
    }

    while (p < sentence + MAX_WORDS) {
        **p = '\0';
        p++;
    }

    printf("Reversal of sentence: ");
    while (p-- >= sentence) {
        if (**p == '\0') {
            continue;
        }

        printf("%s", *p);

        if (p != sentence) {
            printf(" ");
        } else {
            printf("%c", terminating_char);
        }
    }

    return 0;
}