#include <stdio.h>

int main(void) {

    int money = 0;
    int bills[] = {20, 10, 5, 1};

    printf("Enter a dollar amount: ");
    scanf("%d", &money);

    for (int i = 0; i < 4; i++) {
        int bill = bills[i];
        int amt = money % bill;
        printf("$%d bills: %d", bill, amt);
        money -= amt * bill;

    }

    return 0;
}