#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // fork, write, close, excel
#include <assert.h> // assert
#include <time.h>   // delay
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    int fd[2], rc, rc2;

    // create pipe
    int p1 = pipe(fd);
    assert(p1 > -1);

    // Create child process 1
    rc = fork();
    assert(rc > -1);
    if (rc == 0) {
        // Child
        // close standard input (STDIN_FILENO)
        close(STDIN_FILENO);
        // duplicate the input end of pipe (fd[1])
        dup(fd[1]);
        // close unused pipe ends
        close(fd[0]);
        close(fd[1]);
        // establish the output of this process as the input for pipe
        return 0;
    }

    // Create child process 2
    rc2 = fork();
    assert(rc2 > -1);
    if (rc == 0) {
        // Child
        // close standard output (STDOUT_FILENO)
        close(STDOUT_FILENO);
        // duplicate the output end of pipe (fd[0])
        dup(fd[0]);
        // duplicate and close unused pipe ends
        // establish the input of this process as the output for pipe
        close(STDOUT_FILENO);
        printf("I am a child\n");
        return 0;
    }
    close(fd[0]);
	close(fd[1]);
    return 0;
}