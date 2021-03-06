#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/wait.h>

// equivalent to sort < file1 | uniq
void sort_by_parent(int *fd);
void uniq_by_child(int *fd);

int main() {
    int fd[2], r;

    if ((pipe(fd) == -1)) {
        perror("pipe");
        exit(1);
    }

    r = fork();

    if (r < 0) {
        perror("fork");
        exit(1);
    }

    if (r > 0){
        sort_by_parent(fd);
    } else {
        uniq_by_child(fd);
    }
}

void sort_by_parent(int *fd) {
    int filedes = open("file1.txt", O_RDONLY);

    // reconfigure so all input from file1 are redirected to stdin
    if (dup2(filedes, fileno(stdin)) == -1) {
        perror("dup2.1");
        exit(1);
    }

    // reconfigure so all output from stdout is redirected to write part of pipe
    // this is to sent to uniq
    if (dup2(fd[1], fileno(stdout)) == -1) {
        perror("dup2.2");
        exit(1);
    }

    // close read part of pipe
    if (close(fd[0]) == -1) {
        perror("close1");
    }

    // close write since it's redirected to stdout
    if (close(fd[1]) == -1) {
        perror("close2");
    }

    // close file since it won't be used directly
    if (close(filedes) == -1) {
        perror("close3");
    }

    // executes terminal's sort
    execl("/usr/bin/sort", "sort", (char *) 0);
}

void uniq_by_child(int *fd) {
    // reconfigure stdin so that it reads from pipe
    if (dup2(fd[0], fileno(stdin))) {
        perror("dup2");
        exit(1);
    }
    // close the write pipe (see diagram)
    if (close(fd[1]) == -1) {
        perror("close");
    }

    // close the read pip since it will be read from stdin of pipe
    if (close(fd[0]) == -1) {
        perror("close");
    }

    execl("/usr/bin/uniq", "uniq", (char*) 0); // <- execute file from file path, and return 0 if successful
    fprintf(stderr, "ERROR: exec should not return\n"); // <- run if uniq not run
}