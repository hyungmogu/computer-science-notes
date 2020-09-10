#include <stdio.h>
#include <string.h>

int main() {
    char s1[5];
    char s2[32] = "University of";
    strncpy(s1,s2, sizeof(s1));
    s1[4] = '\0';
    printf("%s\n", s1);
    printf("%s\n", s2);
    return 0;
}