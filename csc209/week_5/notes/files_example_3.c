#include <stdio.h>

#define LINE_LENGTH 80

int main() {
    FILE *sample_file;
    int error, score, total;

    sample_file = fopen("example_sources/sample.txt", "r");
    if (sample_file == NULL) {
        perror("Error opening file\n");
        return 1;
    }

    while (fscanf(sample_file, "%d %d", &score, &total) == 2) {
        printf("Score: %d, Total: %d.\n", score, total);
    }

    error = fclose(sample_file);
    if (error != 0) {
        perror("fclose failed on input file\n");
        return 1;
    }

    return 0;
}