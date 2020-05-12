#include <stdio.h>

int sum(int *A, int size) {
    int total = 0;
    for (int i = 0; i < size; i++) {
        total += A[i];
    }

    printf("Size of A: %lu\n", sizeof(A)); // evaluates the size of pointer to an int

    return total;
}

void change(int *A) {
    A[0] = 50;
}

int main() {
    int scores[4] = {4,5,-1,12};
    printf("size of scores %lu\n", sizeof(scores));
    printf("total is %d\n", sum(scores, 4));

    change(scores);
    printf("First element in array has value %d\n", scores[0]);

    return 0;
}