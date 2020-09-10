#include <stdio.h>
#include <string.h>

struct student {
    char first_name[20];
    char last_name[20];
    int year;
    float gpa;

};

void change(struct student *s) { // <- passes by reference
    strcpy((*s).first_name, "Adam");
    (*s).gpa = 4.0;
};

int main(void) {
    struct student good_student;

    strcpy(good_student.first_name, "Jo");
    good_student.gpa = 2.1;
    change(&good_student); // <- to pass function by reference (This is too cool!!!)
    printf("first name is %s\n", good_student.first_name);
    printf("GPA is %f\n", good_student.gpa);

    return 0;
}