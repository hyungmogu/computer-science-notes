#include <stdio.h>
#include <string.h>

int main() {
    char s1[30] = "University of C Programming";
    char *p;
    p = strchr(s1, 'v');

    if (p == NULL) {
        printf("Character not found\n");
    } else {
        printf("Character found at index %d\n", (int)(p - s1));
    }

    return 0;
}