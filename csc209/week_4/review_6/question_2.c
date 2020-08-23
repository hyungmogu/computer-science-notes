#include <stdio.h>
#include <stdlib.h>  // malloc
#include <string.h>  // strlen

char *duplicate(const char *str);

int main(void) {
    char s[] = "hello world", *p;

    p = duplicate (s);

    printf("Duplicate: %s", *p);

    free(p);
    return 0;
}


char *duplicate(const char *str) {
    char *p;
    const char *q;

    int n = strlen(str);

    p = (char *)malloc(n + 1);

    if (!p) {
        return p;
    }

    q = str;
    while (q < str + n) {
        *p++ = *q++;
    }

    *p = '\0';

    return p;
}