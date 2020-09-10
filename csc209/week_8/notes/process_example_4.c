#include <stdio.h>
#include <unistd.h>

int main() {
    printf("About to call excel. My PID is %d\n", getpid());
    execl("./hello.out", NULL); // <- searches for .out
    perror("exec");
    return 1;
}