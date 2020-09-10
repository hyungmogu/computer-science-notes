#include <stdio.h>

void reduce(int numerator, int denominator, int *reduced_numerator, int *reduced_denominator);

int main(void) {

    int numerator,
        denominator,
        reduced_denominator,
        reduced_numerator;

    printf("Enter a fraction: ");
    scanf("%d /%d", &numerator, &denominator);

    reduce(numerator, denominator, &reduced_numerator, &reduced_denominator);

    printf("In lowest terms: %d/%d\n", reduced_numerator, reduced_denominator);

    return 0;
}

void reduce(int numerator, int denominator,
            int *reduced_numerator,
            int *reduced_denominator) {

    int n, m, r;

    m = numerator;
    n = denominator;

    while (n != 0) {
        r = m % n;
        m = n;
        n = r;
    }

    *reduced_numerator = numerator / m;
    *reduced_denominator = denominator / m;
}
