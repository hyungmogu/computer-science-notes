#include <stdio.h>

void apply_late_penalty(char *grade_ptr) {
    if (*grade_ptr != 'F') {
        (*grade_ptr)++;
    }
}

int main() {
    char grade_moe = 'B';
    printf("Moe earned a %c\n", grade_moe);
    apply_late_penalty(&grade_moe);
    printf("Moe was late, so instead he gets a %c\n", grade_moe);

    return 0;
}