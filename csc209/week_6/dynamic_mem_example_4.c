#include <stdio.h>
#include <stdlib.h>

void helper(int **arr_double_p) {
    *arr_double_p = malloc(sizeof(int) * 3);

    int *arr = *arr_double_p;

    arr[0] = 0;
    arr[1] = 21;
    arr[2] = 23;
}

int main() {
    int *data;
    helper(&data);

    printf("middle value: %d\n", data[1]);

    return 0;
}