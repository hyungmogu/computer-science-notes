#include <stdio.h>

int main() {
    int A[3] = {1,2,3};
    int B[5] = {11, 23, 55};

    A[5] = 2; // may overwrite if memory location does exist
    B[3000] = 25; // raises segmentation fault

    return 0;
}