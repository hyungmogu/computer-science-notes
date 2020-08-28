
#include <stdio.h>
#include <string.h>

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


    if (compare_dates(date1, date2) < 0) {
        printf("%02d/%02d/%04d is earlier than %02d/%02d/%04d\n",
                date1.month, date1.day, date1.year,
                date2.month, date2.day, date2.year);
    } else {
        printf("%02d/%02d/%04d is earlier than %02d/%02d/%04d\n",
                date2.month, date2.day, date2.year,
                date1.month, date1.day, date1.year);
    }

    return 0;
}

int compare_dates(struct date date1, struct date date2)
{
    char d1[9], d2[9];

    sprintf(d1, "%04d%02d%02d", date1.year, date1.month, date1.day);
    sprintf(d2, "%04d%02d%02d", date2.year, date2.month, date2.day);

    return strcmp(d1, d2);
}