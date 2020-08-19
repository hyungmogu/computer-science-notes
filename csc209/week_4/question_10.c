#include <stdio.h>

void find_closest_flight(int desired_time, int *departure_time, int *arrival_time);

int main(void) {

    int hour,
        minute,
        departure_hour,
        departure_minutes,
        arrival_hour,
        arrival_minutes,
        desired_time,
        departure_time,
        arrival_time;

    printf("Enter a 24-hour time: ");
    scanf("%d :%d", &hour, &minute);
    desired_time = hour * 60 + minute;

    find_closest_flight(desired_time, &departure_time, &arrival_time);

    // convert to 24 hour time
    departure_hour = departure_time / 60;
    departure_minutes = departure_time % 60;

    arrival_hour = arrival_time / 60;
    arrival_minutes = arrival_time % 60;

    printf("Closest departure time is ");

    // convert to 12 hour time

    printf("%02d:%02d %s., arriving at %02d:%02d %s.\n",
            departure_hour > 12 ? departure_hour - 12 : departure_hour,
            departure_minutes,
            departure_hour >= 12 ? "P.M" : "A.M",
            arrival_hour > 12 ? arrival_hour - 12 : arrival_hour,
            arrival_minutes,
            arrival_hour >= 12 ? "P.M" : "A.M");

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
        *departure_time = 12 * 60 + 47;
        *arrival_time = 15 * 60;
    } else if (desired_time < d5 + (d6 - d5) / 2) {
        *departure_time = 14 * 60;
        *arrival_time = 16 * 60 + 8;
    } else if (desired_time < d6 + (d7 - d6) / 2) {
        *departure_time = 15 * 60 + 45;
        *arrival_time = 17 * 60 + 55;
    } else if (desired_time < d7 + (d8 - d7) / 2) {
        *departure_time = 19 * 60;
        *arrival_time = 21 * 60 + 20;
    } else {
        *departure_time = 21 * 60 + 45;
        *arrival_time = 23 * 60 + 58;
    }
}