#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

struct node {
    int value;
    struct node *next;
};

struct node *delete_from_list(struct node *list, int n);

int main(void)
{
    struct node *l, *l1, *l2, *l3, *l4, *res, *p;

    l = malloc(sizeof(struct node));
    l1 = malloc(sizeof(struct node));
    l2 = malloc(sizeof(struct node));
    l3 = malloc(sizeof(struct node));
    l4 = malloc(sizeof(struct node));

    l->value = 1;
    l->next = l1;
    l1->value = 2;
    l1->next = l2;
    l2->value = 3;
    l2->next = l3;
    l3->value = 4;
    l3->next = l4;
    l4->value = 5;

    res = delete_from_list(l, 3);

    for (p = res; p != NULL; p=p->next) {
        printf("%d\n", p->value);
    }
    return 0;
}

struct node *delete_from_list(struct node *list, int n)
{
    struct node *cur = list, *temp;

    if (cur->value == n) {
        list = cur->next;
        return list;
    }

    for (cur = list; cur != NULL; cur = cur -> next) {

        if (cur->next != NULL && cur->next->value == n) {
        break;
        }
    }

    if (cur == NULL) {
        return list;
    }

    temp = cur->next;
    cur->next = cur->next->next;

    free(temp);
    return list;
}