#include <stdio.h>  // printf
#include <stdlib.h> // atoi
#include <time.h>   // time_t, time
#include <math.h>   // ceil
#include <string.h> // strncmp
#include <unistd.h>

int main(int argc, char *argv[]) {
    int n,
        size_in_bytes,
        size_in_mb;

    time_t start_t, curr_t;

    // get arguments
    if (argc != 3) {
        perror("ERROR: Argument must be of format ./question_3 -m <SIZE IN INTEGER>\n");
        return(-1);
    }

    if (strncmp(argv[1],"-m", 2) != 0) {
        perror("ERROR: Argument must be of format ./question_3 -m <SIZE IN INTEGER>\n");
        return(-1);
    }

    // convert argument (requested amount of memory) from string to integer
    size_in_mb = atoi(argv[2]);

    // convert size in megabytes to bytes
    size_in_bytes = size_in_mb * 1000000;
    // calculate the size of array n needed to fill the requested amount of memory
    n = ceil(size_in_bytes / sizeof(int));
    // create array of size n (using heap memory)
    int array[n];

    // setup time
    start_t = time(NULL);

    while(1) {
        for (int i = 0; i < n; i++) {
            // refresh screen
            #if defined(__linux__) || defined(__APPLE__)
                system("clear");
            #endif

            // add a child process for displaying memory
            int rc = fork();
            if (rc < 0) {
                perror("ERROR: Fork failed");
                exit(1);
            } else if (rc == 0) {
                #if defined(__linux__)
                    execlp("free", "free", "-m", NULL);
                #endif
                exit(0);
            }

            printf("\n");

            int rc2 = fork();
            if (rc2 < 0) {
                perror("ERROR: Fork failed");
                exit(1);
            } else if (rc2 == 0) {
                char ppid[sizeof(getppid()) + 1];
                snprintf(ppid, sizeof(getppid()), "%d", getppid());

                printf("%s\n", ppid);
                #if defined(__linux__)
                    printf("I am here\n");
                    execlp("pmap", "pmap", "-X", ppid, NULL);
                #endif
                exit(0);
            }


            printf("\n");

            // indefinitely traverse through the array, touching elements
            array[n] = i % 5;
            // display current index:
            printf("Current index: %d\n", i);
            // display time elapsed:
            curr_t = time(NULL);
            printf("Time elapsed: %ld seconds\n", (curr_t - start_t));
            // display amount of memory allocated:
            printf("Amount of memory allocated: %d MB\n", size_in_mb);
            // display size n:
            printf("Size of array: %d \n", n);
            // display "press Cmd + Z to kill program"
            printf("Press ctrl + z to terminate program\n");

            sleep(1);
        }
    }

    return 0;
}