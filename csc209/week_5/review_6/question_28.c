#include <stdio.h>

#define SIZE 50

void reverse_name(char *name);

int main(void) {

    char first_name[SIZE], last_name[SIZE], full_name[SIZE];

    printf("Enter a first and last name: ");
    scanf("%s", first_name);
    scanf("%s", last_name);

    strcat(full_name, first_name);
    strcat(full_name, " ");
    strcat(full_name, last_name);

    return 0;
}

void reverse_name(char *name) {

}