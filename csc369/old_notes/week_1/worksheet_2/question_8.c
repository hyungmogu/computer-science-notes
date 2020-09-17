#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <assert.h>
#include <fcntl.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    // setup open()
    int fd = open("./question_8.txt", O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);
    assert(fd > -1);
    // create child process
    int rc = fork();
    if (rc < 0) {
        fprintf(stderr, "Fork failed\n");
        exit(1);
    } else if (rc == 0) {
    // child
        int bytes_written = write(fd, "This is a child\n", 16);
        assert (bytes_written == 16);
    } else {
    // parent
        int bytes_written = write(fd, "This is a parent\n", 17);
        assert (bytes_written == 17);
    }

    close(fd);

    return 0;
}