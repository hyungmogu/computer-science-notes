#include <stdio.h>
#include <stdlib.h>  // malloc
#include <string.h>  // strlen

char *duplicate(const char *str);

int main(void) {
    char s[] = "hello world", *p;

    p = duplicate (s);

    printf("Duplicate: %s\n", p);

    free(p);
    return 0;
}


char *duplicate(const char *str) {
    char *p, *q;
    const char *r;

    int n = strlen(str);

    p = (char *)malloc(n + 1);

    if (!p) {
        return p;
    }

    r = str;
    q = p;
    while (r < str + n) {
        *q = *r;
        q++;
        r++;
    }

    *q = '\0';

    return p;
}