#include <stdio.h>

#define TAX_RATE .80
#define WITH_TAX(x) ((x) * 1.80)

int main() {
    double purchase = 9.99;
    double purchase2 = 12.49;

    printf("%f\n", WITH_TAX(purchase + purchase2));
}