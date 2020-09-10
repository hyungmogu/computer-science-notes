#include <stdio.h>
#include <unistd.h>

int main() {
    int i;
    pid_t result;

    i = 5;
    printf("%d\n", i);

    result = fork();

    if (result > 0) {
        i = i + 2;
    } else if (result == 0) {
        i = i - 2;
    } else {
        perror("fork");
    }

    printf("%d\n", i);
    return 0;
}