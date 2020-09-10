#include <stdio.h>

int main() {
    FILE *output_file;
    int error;
    int total = 50;
    float small_number = 0.125;

    output_file = fopen("example_sources/output.txt", "w");
    if (output_file == NULL) {
        perror("Error opening file\n");
        return 1;
    }

    fprintf(output_file, "The first line in the file\n");
    fprintf(output_file, "The integer is %d\n", total);
    fprintf(output_file, "The small float is %f\n", small_number);

    error = fclose(output_file);
    if (error != 0) {
        perror("fclose failed\n");
        return 1;
    }

    return 0;
}