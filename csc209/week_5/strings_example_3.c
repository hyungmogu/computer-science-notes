#include <stdio.h>
#include <string.h>

int main() {
    char weekday[10] = "Monday";
    printf("Length of string: %lu\n", strlen(weekday));
    printf("Length of string: %lu\n", sizeof(weekday));
    return 0;
}