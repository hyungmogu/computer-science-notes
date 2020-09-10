#include <stdio.h>

#define LINE_LENGTH 80

int main() {
    char line[LINE_LENGTH + 1];

    while (fgets(line, LINE_LENGTH + 1, stdin) != NULL) {
        printf("%s", line);
    }

    return 0;
}