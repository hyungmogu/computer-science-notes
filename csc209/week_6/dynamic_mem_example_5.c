#include <stdio.h>
#include <stdlib.h>

int main(){
    int **double_pointers = malloc(sizeof(int) * 2);

    double_pointers[0] = malloc(sizeof(int));
    double_pointers[1] = malloc(sizeof(int) * 2);

    double_pointers[0][0] = 12;
    double_pointers[1][0] = 2;
    double_pointers[1][1] = 3;
    double_pointers[1][2] = 4;

    free(double_pointers[0]);
    free(double_pointers[1]);
    free(double_pointers);
}