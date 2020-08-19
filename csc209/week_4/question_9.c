#include <stdio.h>

void pay_amount(int dollars, int *twenties, int *tens,
                int *fives, int *ones);

int main(void) {

    int dollars, twenties, tens, fives, ones;

    printf("Enter a dollar amount: ");
    scanf("%d", &dollars);

    pay_amount(dollars, &twenties, &tens, &fives, &ones);

    printf("$20 bills: %d\n", twenties);
    printf("$10 bills: %d\n", tens);
    printf("$5 bills: %d\n", fives);
    printf("$1 bills: %d\n", ones);

    return 0;
}

void pay_amount(int dollars, int *twenties, int *tens,
                int *fives, int *ones) {

    int bills[] = {20, 10, 5, 1};

    for (int i = 0; i < 4; i++) {
        int bill = bills[i];
        int amt = dollars / bill;

        if (bill == 20) {
            *twenties = amt;
        } else if (bill == 10) {
            *tens = amt;
        } else if (bill == 5) {
            *fives = amt;
        } else {
            *ones = amt;
        }

        dollars -= amt * bill;
    }
}