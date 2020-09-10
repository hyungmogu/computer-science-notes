#include <stdio.h>

int main() {
    FILE *sample_file;

    sample_file = fopen("example_sources/sample.txt", "r");
    if (sample_file == NULL) {
        fprintf(stderr, "Error opening file \n");
        return 1;
    }

    printf("File opened: we can use it here\n");

    if (fclose(sample_file) != 0) {
        fprintf(stderr, "fclose failed\n");
        return 1;
    }

    return 0;
}