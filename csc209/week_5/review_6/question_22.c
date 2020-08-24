/* deal.c (Chapter 8, page 173) */
/* Deals a random hand of cards */

#include <stdio.h>

int main(int argc, char *argv[])
{
    for(int i = argc - 1; i >= 1; i--) {
        printf("%s", argv[i]);

        if (i != 1) {
            printf(" ");
        }
    }

    printf("\n");
    return 0;
}