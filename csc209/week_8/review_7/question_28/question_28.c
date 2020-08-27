
#include <stdio.h>

struct date {
    int year;
    int month;
    int day;
};

int compare_dates(struct date date1, struct date date2);

int main(void) {

    struct date date1, date2;

    printf("Enter first date (mm/dd/yy): ");
    scanf("%d/%d/%d", &date1.month, &date1.day, &date1.year);
    printf("Enter second date (mm/dd/yy): ");
    scanf("%d/%d/%d", &date2.month, &date2.day, &date2.year);


    if (compare_dates(date1, date2)) {
        printf("%d/%d/%.2d is earlier than %d/%d/%.2d\n", m2, d2, y2, m1, d1, y1);
    } else {
        printf("%d/%d/%.2d is earlier than %d/%d/%.2d\n", m2, d2, y2, m1, d1, y1);
    }

    return 0;
}

int compare_dates(const struct date date1, struct date date2)
{

}