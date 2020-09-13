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
    union ieee_float i_float_1;
    i_float_1.parts.fraction = 0;
    i_float_1.parts.exponent = 128;
    i_float_1.parts.sign = 1;

    printf("%f\n", i_float_1.value);
    return 0;
}
