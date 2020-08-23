#include <stdio.h>
#include <string.h>

char *duplicate(const char *str);

int main(void) {
    char s[] = "hello world", *p;

    p = duplicate (s);

    printf("Duplicate: %s", *p);
    return 0;
}


char *duplicate(const char *str) {
    char *p;
    int n = strlen(str);

    p = (char *)malloc(n + 1);

    if (!p) {
        return p;
    }

    for (p = str; p < str + n; p++) {
        *p = *str;
    }

    return p;
}