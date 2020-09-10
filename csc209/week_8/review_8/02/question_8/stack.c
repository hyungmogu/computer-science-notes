#include "stack.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdbool.h>

struct node {
    int value;
    struct node *next;
} *top;

void make_empty(void)
{
    struct node *to_be_freed;

    while (top != NULL)
    {
        to_be_freed = top;
        top = top->next;
        free(to_be_freed);
    }
}

bool is_empty(void)
{
    if (top == NULL) {
        return true;
    }

    return false;
}

bool push(int i)
{
    struct node *n, *temp;
    n = malloc(sizeof(struct node));
    if (n == NULL) {
        return false;
    }

    n->value = i;
    n->next = top;
    top = n;

    return true;
}

int pop(void)
{
    struct node *to_be_freed;
    int res;

    res = top->value;
    to_be_freed = top;
    top = top->next;

    free(to_be_freed);

    return res;
}