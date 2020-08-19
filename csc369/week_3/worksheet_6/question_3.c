#include <stdio.h>  // printf
#include <time.h>   // clock_t, clock, CLOCKS_PER_SEC
#include <unistd.h>

int main(int argc, char *argv[]) {
    int n;
    clock_t start_t, curr_t;

    // get arguments

    // convert argument (amount of memory used) from string to integer
    // calculate the size of array n needed to fill the requested amount of memory
    n = 10;
    // create array of size n (using stack memory)
    int array[n];

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

            printf("Amount of memory allocated: %f MB\n");
            // display "press Cmd + Z to kill program"
            printf("Press ctrl + z (or cmd + z) to terminate program\n");
            // refresh screen
        }
    }
}