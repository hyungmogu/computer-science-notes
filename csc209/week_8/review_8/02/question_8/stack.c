#include "stack.h"
#include <stddef.h>
#include <stdbool.h>

struct node {
    int value;
    struct node *next;
} *top;

void make_empty(void)
{

}

int is_empty(void)
{

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

}