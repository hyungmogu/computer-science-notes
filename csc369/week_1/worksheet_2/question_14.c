#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // fork, write, close, excel
#include <assert.h> // assert
#include <string.h> // strlen
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    int fd[2], rc, rc2;
    char *msg1 = "hello world";
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
        // close unused pipe ends (fd[STDOUT_FILENO])
        close(fd[STDOUT_FILENO]);
        // establish the output of this process as the input for pipe
        write(fd[STDIN_FILENO], msg1, strlen(msg1) + 1);
        return 0;
    }

    // Create child process 2
    rc2 = fork();
    assert(rc2 > -1);
    if (rc == 0) {
        // Child
        char response[strlen(msg1) + 1];
        // close unused pipe ends (fd[STDIN_FILENO])
        close(fd[STDIN_FILENO]);
        // establish the input of this process as the output for pipe
        read(fd[STDOUT_FILENO], response, strlen(response) + 1);
        printf("RESULT: %s", response);
        return 0;
    }
    printf("**Parent process ending**");
    close(fd[0]);
	close(fd[1]);
    return 0;
}