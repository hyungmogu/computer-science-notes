#include <stdio.h>
#define DAYS 4

int main() {
    int i;
    i = 5;
    printf("Value of i: %d\n", i);
    printf("Address of i: %p\n", &i);

    int *pt;
    pt = &i;

    printf("value of pt: %p\n", pt);
    printf("Address of pt: %p\n", &pt);

    printf("Value pointed to by pt: %d\n", *pt);

    return 0;
}