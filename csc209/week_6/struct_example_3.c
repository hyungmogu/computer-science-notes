#include <stdio.h>
#include <string.h>

struct student {
    char first_name[20];
    char last_name[20];
    int year;
    float gpa;

};

int main(void) {
    struct student s;
    struct student *p;

    strcpy(s.first_name, "Jo"); //strcpy used because char is an array.
    strcpy(s.last_name, "Smith");
    s.year = 2;
    s.gpa = 3.2;

    p = &s;
    (*p).gpa = 3.0;
    p->year = 3;

    strcpy(p->first_name, "Hello");

    printf("Name: %s %s\n", s.first_name, s.last_name);
    printf("Year %d. GPA %.2f\n", s.year, s.gpa);

    return 0;
}