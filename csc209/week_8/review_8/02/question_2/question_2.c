#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *duplicate(char *str);

int main(void) {
    char *s = "hello world", *p;

    p = duplicate(s);

    printf("%s\n", p);

    free(p);
}

char *duplicate(char *str) {
    char *res;

    res = malloc(strlen(str) + 1);
    if (res == NULL) {
        return res;
    }

    strcpy(res, str);

    return res;
}