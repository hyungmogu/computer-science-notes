#include <stdio.h>
#include <stdlib.h>

int *my_malloc(int n);

int main(void) {
    int n = 5, *p;

    p = my_malloc(n);

    free(p);
}

int *my_malloc (int n) {
    int *res;

    res = malloc(n * sizeof(int));
    if (res == NULL) {
        perror("Allocation failed.");
    }

    return res;
}