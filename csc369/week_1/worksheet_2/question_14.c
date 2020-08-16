#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // fork, write, close, excel
#include <assert.h> // assert
#include <time.h>   // delay
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    int fd[2], rc, rc2;

    // Create child process 1
    rc = fork();
    assert(rc > -1);
    if (rc == 0) {
        // Child
        // establish the output of this process as the input for pipe
        close(STDOUT_FILENO);
        printf("I am a child\n");
        return 0;
    }

    // Create child process 2
    rc2 = fork();
    assert(rc2 > -1);
    if (rc == 0) {
        // Child
        // establish the input of this process as the output for pipe
        close(STDOUT_FILENO);
        printf("I am a child\n");
        return 0;
    }
    close(fd[0]);
	close(fd[1]);
    return 0;
}