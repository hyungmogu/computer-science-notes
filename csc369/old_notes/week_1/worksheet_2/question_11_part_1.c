#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // fork, write, close, excel
#include <assert.h> // assert
#include <time.h>   // delay
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    int rc = fork();
    assert(rc > -1);
    if (rc == 0) {
        // child
        // Comment the rest of exec commands to continue
        printf("I am a child\n");
    } else {
        // parent
        int rc_wait = wait(NULL);
        printf("I am a parent\n");
    }
    return 0;
}