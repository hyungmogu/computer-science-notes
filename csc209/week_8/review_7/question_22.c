#include <stdio.h>

struct dialing_code {
    char *country;
    int code;
};

int main(void) {
    const struct dialing_code country_codes[] = {
        {"Argentina", 54}, {"Bangladesh", 880},
        {"Brazil", 55}, {"Burma (Myanmar)", 95},
        {"China", 86}, {"Colombia", 57},
        {"Congo, Dem. Rep. of", 243}, {"Egypt", 20},
        {"Ethiopia", 251}, {"France", 33},
        {"Germany", 49}, {"India", 91},
        {"Indonesia", 62}, {"Iran", 98},
        {"Italy", 39}, {"Japan", 81},
        {"Mexico", 52}, {"Nigeria", 234},
        {"Pakistan", 92}, {"Philippines", 63},
    };

    return 0;
}
