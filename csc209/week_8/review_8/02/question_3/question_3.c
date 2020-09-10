#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

int *create_array(int n, int initial_value);

int main(void) {
    int n = 10, initial_value = 1, *p, *q;

    p = create_array(n, initial_value);

    for (q = p; q < p + n; q++) {
        printf("%d\n", *q);
    }

    free(p);
}

int *create_array(int n, int initial_value) {
    int *p, *res;

    res = malloc(n * sizeof(int));

    if (res == NULL) {
        return res;
    }

    for (p = res; p < res + n; p++) {
        *p = initial_value;
    }

    return res;
}