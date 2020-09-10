#include <stdio.h>

int main() {
    int A[3] = {13,55,20};
    int *p = A;

    printf("%d\n",*p);
    printf("%d\n",*(p+1));
    printf("%d\n",p[0]);
    printf("%d\n",p[1]);

    p = p + 1;
    printf("%d\n",*p);
    printf("%d\n",p[0]);
    printf("%d\n",p[1]);
    printf("%d\n",*(p-1));

    return 0;
}