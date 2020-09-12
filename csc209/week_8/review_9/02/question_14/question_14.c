#include <stdio.h>
#include <stdlib.h>

union ieee_float {
    float value;
    struct {
        unsigned int fraction: 23;
        unsigned int exponent: 8;
        unsigned int sign: 1;
    } parts;
};

int main() {
    union ieee_float f1;

    f1.parts.fraction = 20;
    f1.parts.exponent = 8;

    printf("%f\n", f1.value);
    return 0;
}
