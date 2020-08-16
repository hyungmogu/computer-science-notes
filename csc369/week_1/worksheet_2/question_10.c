#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // fork, write, close, excel
#include <assert.h> // assert
#include <time.h>   // delay
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    char *envp[] =  {"HOME=/usr/moegu", "LOGNAME=moegu", NULL}; // HOME - directory of user, LOGNAME - username
    int rc = fork();
    assert(rc > -1);
    if (rc == 0) {
    // child
        printf("I am a child\n");
        execl("/bin/ls", "-l", NULL);
        execlp("ls", "-l", NULL);
        execle("/bin/ls", "ls", "-l", NULL, envp);
        printf("--------");
    } else {
    // parent
        printf("I am a parent\n");
    }
    return 0;
}