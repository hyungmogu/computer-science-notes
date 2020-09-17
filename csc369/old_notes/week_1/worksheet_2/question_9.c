#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // fork, write, close
#include <assert.h> // assert
#include <time.h>   // delay
#include <sys/wait.h>

void delay(int milliseconds)
{
    long pause;
    clock_t now,then;

    pause = milliseconds*(CLOCKS_PER_SEC/1000);
    now = then = clock();
    while( (now-then) < pause )
        now = clock();
}

int main(int argc, char *argv[]) {
    // setup open()
    // create child process
    int rc = fork();
    assert(rc > -1);
    if (rc == 0) {
    // child
        printf("hello\n");
    } else {
    // parent
        delay(1000);
        printf("goodbye\n");
    }
    return 0;
}