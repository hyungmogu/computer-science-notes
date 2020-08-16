#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // fork, write, close, excel
#include <assert.h> // assert
#include <time.h>   // delay
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    for (int i = 0; i < 5; i++) {
        int rc = fork();
        assert(rc > -1);
        if (rc == 0) {
            // child
            int rc_wait_child = wait(NULL); // Returns -1
            printf("I am a child (PID: %d)\n", getpid());
            printf("Value of Wait (PID: %d): %d\n", rc_wait_child, getpid());
            printf("------\n");
            return 0;
        }
    }
    // parent
    int rc_wait = wait(NULL); // returns PID of most-recently terminated child
    printf("I am a parent\n");
    printf("Value of Wait (PID %d): %d\n", rc_wait, getpid());
    printf("------\n");

    return 0;
}