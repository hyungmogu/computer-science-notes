#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define SIZE 50

void reverse_name(char *name);

int main(void) {

    char name[SIZE], *p = name;

    printf("Enter a first and last name: ");
    scanf("%s", p);
    printf("%s\n", name);

    strcat(p, " ");

    while(*p++)
        ;

    scanf("%s", p);

    reverse_name(name);

    printf("%s\n", name);
    return 0;
}

void reverse_name(char *name) {
    int n = strlen(name);
    char first_name[n], last_name[n], *pa = name,
         *pb = first_name, *pc = last_name;

    printf("%s\n", name);
    bool is_first_name = true;

    for (; *pa != '\0'; pa++) {
        if (*pa == ' ') {
            is_first_name = false;
            continue;
        }

        if (is_first_name) {
            printf("I am here\n");
            *pb = *pa;
            pb++;
        } else {
            *pc = *pa;
            pc++;
        }
    }

    *pb = '\0';
    *pc = '\0';

    printf("%s\n", last_name);
    printf("%s\n", first_name);

    sprintf(name, "%s, %c.", last_name, first_name[0]);
}