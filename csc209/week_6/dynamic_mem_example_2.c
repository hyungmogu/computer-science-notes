#include <stdio.h>
#include <stdlib.h>

int *squares(int max_val) {
    int *result = malloc(max_val * sizeof(int));

    for (int i = 0; i < max_val; i++){
        result[i] = (i+1)*(i+1);
    }

    return result;
}


int main() {
    int *squares_to_10 = squares(10);

    for (int i = 0; i < 10; i++) {
        printf("%d\t", squares_to_10[i]);
    }

    printf("\n");
    return 0;
}