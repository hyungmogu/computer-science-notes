#include <stdio.h>

int main() {
    float daytime_high[4];

    daytime_high[0] = 1.0;
    daytime_high[1] = 2.0;
    daytime_high[2] = 3.0;
    daytime_high[3] = 4.0;

    float average_temp = (daytime_high[0] + daytime_high[1] + daytime_high[2] + daytime_high[3]) / 4;

    int index = 1;

    printf("On day %d, the high was %f.\n", index, daytime_high[index]);

    return 0;
}