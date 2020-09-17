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
        // close read end of pipe (fd[0])
        close(fd[0]);
        // write to pipe
        write(fd[1], msg1, strlen(msg1) + 1);
        close(fd[1]);
        exit(0);
    }

    // Create child process 2
    rc2 = fork();
    assert(rc2 > -1);
    if (rc2 == 0) {
        // Child
        char response[strlen(msg1) + 1];
        // close write end of pipe (fd[1])
        close(fd[1]);
        // read pipe
        read(fd[0], response, strlen(msg1) + 1);
        printf("RESULT: %s\n", response);
        close(fd[0]);
        exit(0);
    }
    printf("**Parent process ending**\n");
    close(fd[0]);
	close(fd[1]);
    return 0;
}