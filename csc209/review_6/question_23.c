/* deal.c (Chapter 8, page 173) */
/* Deals a random hand of cards */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int sum = 0;

    for(int i = 0; i < argc; i++) {
        sum += atoi(argv[i]);
    }

    printf("Total: %d\n", sum);
    return 0;
}