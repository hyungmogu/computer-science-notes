#include <stdio.h>

struct node {
    int value;
    struct node *next;
};

int count_occurrences (struct node *list , int n);

int main(void)
{
    struct node n1, n2, n3;
    int c1, c2;

    n1.value = 1;
    n1.next = &n2;
    n2.value = 2;
    n2.next = &n3;
    n3.value = 2;

    c1 = count_occurrences(&n1, 1);
    c2 = count_occurrences(&n1, 2);

    printf("%d\n", c1);
    printf("%d\n", c2);

    return 0;
}

int count_occurrences (struct node *list , int n)
{
    struct node *p;
    int count = 0;

    for (p = list; p != NULL; p = p->next)
    {
        if (p->value == n) {
            count += 1;
        }
    }

    return count;
}
