#include <stdio.h>

int main() {
    char text1[20] = {'h','e','l','l','o','\n'};
    char text2[20] = "hello";
    char text3[] = "hello";
    char *text4 = "hello";

    printf("%s\n", text1);
    printf("%s\n", text2);
    printf("%s\n", text3);
    printf("%s\n", text4);
    return 0;
}