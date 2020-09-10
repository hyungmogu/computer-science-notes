#include <stdio.h>
#include <unistd.h>
#include <stdio.h>

#define S_IRUSR 0000400 //R for owner
#define S_IRGRP 0000400 //R for group
#define S_IROTH 0000400 //R for others

// Don't run this!!

int main () {
    mode_t mode1 = S_IRUSR | S_IRGRP | S_IROTH; // Example 1
    mode_t mode2 = 0400 | 040 | 004; // Example 2 (<- Notice bitwise or is used)
    mode_t mode3 = 0444; // Example 3
    return(0);
}
