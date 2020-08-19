#include <stdio.h>

void find_closest_flight(int desired_time, int *departure_time, int *arrival_time);

int main(void) {

    int hour, minute, desired_time, departure_time, arrival_time;

    printf("Enter a 24-hour time: ");
    scanf("%d :%d", &hour, &minute);
    desired_time = hour * 60 + minute;

    find_closest_flight(desired_time, &departure_time, &arrival_time);

    printf("Closest departure time is ");

    return 0;
}

void find_closest_flight(int desired_time, int *departure_time, int *arrival_time) {

    int d1 = 480,
        d2 = 583,
        d3 = 679,
        d4 = 767,
        d5 = 840,
        d6 = 945,
        d7 = 1140,
        d8 = 1305;

    if (desired_time <= d1 + (d2 - d1) / 2) {
        *departure_time = 8 * 60;
        *arrival_time = 10 * 60 + 16;
    } else if (desired_time < d2 + (d3 - d2) / 2) {
        *departure_time = 9 * 60 + 43;
        *arrival_time = 11 * 60 + 52;
    } else if (desired_time < d3 + (d4 - d3) / 2) {
        *departure_time = 11 * 60 + 19;
        *arrival_time = 13 * 60 + 31;
    } else if (desired_time < d4 + (d5 - d4) / 2) {
        printf("12:47 p.m., arriving at 3:00 p.m.\n");
    } else if (desired_time < d5 + (d6 - d5) / 2) {
        printf("2:00 p.m., arriving at 4:08 p.m.\n");
    } else if (desired_time < d6 + (d7 - d6) / 2) {
        printf("3:45 p.m., arriving at 5:55 p.m.\n");
    } else if (desired_time < d7 + (d8 - d7) / 2) {
        printf("7:00 p.m., arriving at 9:20 p.m.\n");
    } else {
        printf("9:45 p.m., arriving at 11:58 p.m.\n");
    }
}