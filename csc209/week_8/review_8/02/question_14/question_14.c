#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

struct node {
    int value;
    struct node *next;
};

struct node *delete_from_list(struct node **list, int n);

int main(void)
{
    struct node *n1, *n2, *n3, *res;

    n1 = malloc(sizeof(struct node));
    n2 = malloc(sizeof(struct node));
    n3 = malloc(sizeof(struct node));

    n1->value = 1;
    n1->next = &n2;
    n2->value = 2;
    n2->next = &n3;
    n3->value = 2;

    for (p = res; p != NULL; p=p->next) {
        printf("%d\n", p->value);
    }

    return 0;
}

struct node *delete_from_list(struct node **list, int n)
{
    struct node *cur, *prev;

    for (cur = list, prev = NULL;
            cur != NULL && cur->value != n;
            prev = cur, cur = cur->next)

            ;

    if (cur == NULL) {
        return list;
    }

    if (prev == NULL) {
        list = list->next;
    } else {
        prev->next = cur->next;
    }

    free(cur);
    return list;
}