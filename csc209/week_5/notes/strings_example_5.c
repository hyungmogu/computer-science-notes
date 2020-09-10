#include <stdio.h>
#include <string.h>

int main() {
    char s1[30];
    char s2[14] = "University of";
    char s3[15] = "C Programming";

    strncpy(s1,s2, sizeof(s1));
    s1[sizeof(s1)-1] = '\0';
    strncat(s1, s3, sizeof(s1) - strlen(s1) -1); // -1 is for \0.
    printf("%s\n", s1);
    printf("%s\n", s2);
    printf("%s\n", s1);
    return 0;
}