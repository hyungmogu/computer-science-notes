#include <stdio.h>

#define LINE_LENGTH 80

int main() {
    FILE *sample_file;
    int error;
    char line[LINE_LENGTH + 1];

    sample_file = fopen("example_sources/sample.txt", "r");

    while (fgets(line, LINE_LENGTH + 1, sample_file) != NULL) {
        printf("%s", line);
    }

    error = fclose(sample_file);
    if (error != 0) {
        fprintf(stderr, "fclose failed\n");
        return 1;
    }

    return 0;
}