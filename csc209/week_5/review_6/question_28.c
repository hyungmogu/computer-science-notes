#include <stdio.h>
#include <stdbool.h>

#define SIZE 50

void reverse_name(char *name);

int main(void) {

    char name[SIZE];

    printf("Enter a first and last name: ");
    scanf("%s", name);
    strcat(name, ' ');
    scanf("%s", name);

    reverse_name(name);

    printf("%s\n", name);
    return 0;
}

void reverse_name(char *name) {
    int n = strlen(name);
    char first_name[n], last_name[n], *pa = name,
         *pb = first_name, *pc = last_name;

    bool is_first_name = true;

    for (; *pa != '\0'; pa++) {
        if (*pa == ' ') {
            is_first_name = false;
            continue;
        }

        if (is_first_name) {
            *first_name = *p;
        }
    }
}