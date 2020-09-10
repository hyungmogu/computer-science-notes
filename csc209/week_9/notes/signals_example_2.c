#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void handler(int);

int main () {
    struct sigaction newact;
    newact.sa_handler = handler; // <- like catch statement in python
    newact.sa_flags = 0;
    sigemptyset(&newact.sa_mask);
    sigaction(SIGINT, &newact, NULL);

    for (int i = 0;;) {
        if ((i++ % 5000000000) == 0) {
            fprintf(stderr, ".");
        }
    }
    return(0);
}

void handler(int code) {
    fprintf(stderr, "Signal %d caught\n", code);
    //exit(1);
}
