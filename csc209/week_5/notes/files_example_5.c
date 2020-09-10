#include <stdio.h>

int main() {
    FILE *sample_file, *output_file;
    int error_open, error_closed, score;
    int total = 50;

    sample_file = fopen("example_sources/sample.txt", "r");
    if (sample_file == NULL) {
        fprintf(stderr, "Error opening file \n");
        return 1;
    }

    output_file = fopen("example_sources/output.txt", "w");
    if (output_file == NULL) {
        perror("Error opening file\n");
        return 1;
    }

    while (fscanf(sample_file, "%d %d", &score, &total) == 2) {
        printf("Score: %d\n", score);
        fprintf(output_file, "Score: %d\n", score);
    }

    error_open = fclose(sample_file);
    if (error_open != 0) {
        perror("fclose failed\n");
        return 1;
    }

    error_closed = fclose(output_file);
    if (error_closed != 0) {
        perror("fclose failed\n");
        return 1;
    }

    return 0;
}