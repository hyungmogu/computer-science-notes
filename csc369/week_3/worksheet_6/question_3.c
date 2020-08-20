#include <stdio.h>  // printf
#include <stdlib.h> // atoi
#include <time.h>   // clock_t, clock, CLOCKS_PER_SEC
#include <math.h>   // ceil
#include <string.h> // strncmp
#include <unistd.h>

int main(int argc, char *argv[]) {
    int n,
        size_in_bytes,
        size_in_mb,
        *array;

    clock_t start_t, curr_t;

    // get arguments
    if (argc != 3) {
        perror("Argument must be of format ./question_3 -m <SIZE IN INTEGER>");
        return(-1);
    }

    if (strncmp(argv[1],"-m", 2) != 0) {
        perror("Argument must be of format ./question_3 -m <SIZE IN INTEGER>");
        return(-1);
    }

    // convert argument (requested amount of memory) from string to integer
    size_in_mb = atoi(argv[2]);

    // convert size in megabytes to bytes
    size_in_bytes = size_in_mb * 1000000;
    // calculate the size of array n needed to fill the requested amount of memory
    n = ceil(size_in_bytes / sizeof(int));
    // create array of size n (using heap memory)
    array = malloc(sizeof(int) * n);

    // setup time
    start_t = clock();

    while(1) {
        for (int i = 0; i < n; i++) {
            // indefinitely traverse through the array, touching elements
            array[n] = i % 5;
            // display current index:
            printf("Current index: %d\n", i);
            // display time elapsed:
            curr_t = clock() - start_t;
            printf("Time elapsed: %f seconds\n", ((float)curr_t)/CLOCKS_PER_SEC);
            // display amount of memory allocated:
            printf("Amount of memory allocated: %d MB\n", size_in_mb);
            // display "press Cmd + Z to kill program"
            printf("Press ctrl + z (or cmd + z) to terminate program\n");
            // refresh screen
            fflush(stdout);
            sleep(1);
        }
    }

    free(array);

    return 0;
}