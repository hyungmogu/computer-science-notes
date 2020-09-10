#include <stdio.h>

int main(void) {

    char *s1[] = {"ten", "eleven", "twelve", "thirteen"
                    "fourteen", "fifteen", "sixteen",
                    "seventeen", "eighteen", "nineteen"};

    char *sf[] = {
        "twenty", "thirty", "fourty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    };

    char *ss[] = {
        "one", "two", "three", "four", "five", "six",
        "sven", "eight", "nine"
    };

    int first_digit, second_digit;

    printf("Enter a two-digit number: ");
    scanf("%1d%1d", &first_digit, &second_digit);

    if (first_digit == 1) {
        printf("You entered the number %s", s1[second_digit]);
        return 0;
    }

    if (second_digit == 0) {
        printf("You entered the number %s", sf[first_digit-2]);
        return 0;
    }

    printf("You entered the number %s-%s", sf[first_digit-2], ss[second_digit-1]);

    return 0;
}