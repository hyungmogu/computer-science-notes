#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

// I need to write a program that calls fork()
// Requirements
//  - Before calling fork(), create a variable and set its value to something (e.g 100)

int main(int argc, char *argv[]) {
    int x = 1000;
    int rc = fork();

    if (rc < 0) {
        fprintf(stderr, "Fork failed\n");
        exit(1);
    } else if (rc == 0){
        printf("hello, I am child (pid: %d)\n", (int) getpid());
        printf("value of x is: %d", x);
        printf("---------");
    } else {
        printf("hello, I am parent %d (pid: %d)\n",rc, (int) getpid());
        printf("---------");
    }

    return 0;
}