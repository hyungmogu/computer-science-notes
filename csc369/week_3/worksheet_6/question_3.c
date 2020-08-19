#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    int n;

    // get arguments

    // convert argument (amount of memory used) from string to integer
    // calculate the size of array n needed to fill the requested amount of memory
    n = 10;

    // create array of size n (using stack memory)
    int array[n];


    while(1) {
        for (int i = 0; i < n; i++) {
            // indefinitely traverse through the array, touching elements
            array[n] = i % 5;
            // while traversing, the following should be displayed
            //  Current index:
            //  Time:
            //  Amount of memory allocated:
            //  Press Cmd + Z to kill program
        }
    }
}