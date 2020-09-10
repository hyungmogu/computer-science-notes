#include "stack.h"
#include <stdio.h>

int main(void)
{
    int r1, r2;
    push(1);
    push(2);

    r1 = pop();
    r2 = pop();

    printf("%d\n", r1);
    printf("%d\n", r2);

    make_empty();
    return 0;
}