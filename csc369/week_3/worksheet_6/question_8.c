#include <stdio.h>  // printf
#include <stdlib.h> // atoi
#include <time.h>   // time_t, time
#include <math.h>   // ceil
#include <string.h> // strncmp
#include <unistd.h>
#include <sys/wait.h> // wait

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

    // get pid of parent
    char parent_pid[sizeof(getpid()) + 2];
    snprintf(parent_pid, sizeof(getpid()) + 2, "%d", getpid());

    while(1) {
        #if defined(__linux__) || defined(__APPLE__)
            system("clear");
        #endif

        // add a child process for displaying memory
        int rc = fork();
        if (rc < 0) {
            perror("ERROR: Fork failed");
            exit(1);
        } else if (rc == 0) {

            int rc2 = fork();
            if (rc2 < 0) {
                perror("ERROR: Fork failed");
                exit(1);
            } else if (rc2 == 0) {
                #if defined(__linux__)
                    execlp("pmap", "pmap", "-X", parent_pid, NULL);
                #endif
                exit(0);
            }

            printf("\n");
            wait(NULL);


            #if defined(__linux__)
                execlp("free", "free", "-m", NULL);
            #endif
            exit(0);
        }

        // display "press Cmd + Z to kill program"
        printf("Press ctrl + z to terminate program\n");

        for (int i = 0; i < n; i++) {
            // indefinitely traverse through the array, touching elements
            array[n] = i % 5;
        }

        sleep(1);
    }

    return 0;
}