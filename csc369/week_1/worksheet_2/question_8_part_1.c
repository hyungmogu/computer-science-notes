#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    // setup open()
    int fd = open("./question_8.txt", O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);

    // create child process
    if (fd < 0) {
        fprintf(stderr, "Open Failed\n");
        exit(1);
    } else {
        int rc = fork();

        if (rc < 0) {
            fprintf(stderr, "Fork failed\n");
        } else if (rc == 0) {
        // child

        } else {
        // parent

        }
    }

    // read all lines in file question_8.txt

    return 0;
}