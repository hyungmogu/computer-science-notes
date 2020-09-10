#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

struct node {
    int value;
    struct node *next;
};

struct node *find_last(struct node *list, int n);

int main(void) {

    struct node n1, n2, n3, *res;

    n1.value = 1;
    n1.next = &n2;
    n2.value = 2;
    n2.next = &n3;
    n3.value = 1;

    res = find_last(&n1, 1);

    printf("%d", res->value);

    return 0;
}

struct node *find_last(struct node *list, int n)
{
    struct node *res = NULL, *p;

    for (p = list; p != NULL; p = p->next) {
        if (p->value == n) {
            res = p;
        }
    }

    return res;
}