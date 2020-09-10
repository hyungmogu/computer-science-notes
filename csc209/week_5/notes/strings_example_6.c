#include <stdio.h>
#include <string.h>

int main() {
    char s1[30] = "University of C Programming";
    char *p1, *p2;
    p1 = strchr(s1, 'v');
    p2 = strstr(s1, "Prog");

    if (p1 == NULL) {
        printf("Character not found\n");
    } else {
        printf("Character found at index %d\n", (int)(p1 - s1));
    }

    if (p2 == NULL) {
        printf("String not found\n");
    } else {
        printf("String found at index %d\n", (int)(p2 - s1));
    }

    return 0;
}