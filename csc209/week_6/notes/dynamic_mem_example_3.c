#include <stdio.h>
#include <stdlib.h>

int play_with_memory() {
    int i;
    int *pt = malloc(sizeof(int));

    i = 15;
    *pt = 15;

    free(pt);

    return 0;
}


int main() {
    play_with_memory();
    play_with_memory();
    play_with_memory();
    play_with_memory();
    play_with_memory();

    return 0;
}