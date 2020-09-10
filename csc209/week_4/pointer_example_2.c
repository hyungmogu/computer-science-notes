#include <stdio.h>
#define DAYS 4

int main() {
    int i = 7;
    int *pt;
    pt = &i;
    *pt = 9;

    printf("Value of i: %d\n", i);
    printf("Address of i: %p\n", &i);

    printf("pt points to %d\n", *pt);

    return 0;
}