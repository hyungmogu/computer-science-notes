#include <stdio.h>

#define N 8

struct flight_times {
    int departure_time;
    int arrival_time;
};


int find_closest_departure_time(int user_time, const struct flight_times ft[], int n);

int main(void) {
    int user_time,
        hour,
        minute,
        departure_hour,
        departure_minutes,
        arrival_hour,
        arrival_minutes;

    struct flight_times ft[N] = {
        {480, 616}, {583, 712}, {679, 811}, {767, 900},
        {840, 968}, {945, 1075}, {1140, 1280}, {1305, 1438}
    };

    printf("Enter a 24-hour time: ");
    scanf("%d :%d", &hour, &minute);
    user_time = hour * 60 + minute;

    int index = find_closest_departure_time(user_time, ft, N);

    // convert to 24 hour time
    departure_hour = ft[index].departure_time / 60;
    departure_minutes = ft[index].departure_time % 60;

    arrival_hour = ft[index].arrival_time / 60;
    arrival_minutes = ft[index].arrival_time % 60;

    printf("Closest departure time is ");

    printf("%02d:%02d %s., arriving at %02d:%02d %s.\n",
        departure_hour > 12 ? departure_hour - 12 : departure_hour,
        departure_minutes,
        departure_hour >= 12 ? "P.M" : "A.M",
        arrival_hour > 12 ? arrival_hour - 12 : arrival_hour,
        arrival_minutes,
        arrival_hour >= 12 ? "P.M" : "A.M");

    return 0;
}

int find_closest_departure_time(int user_time, const struct flight_times ft[], int n) {

    int closest_index, closest_time_distance = 2000, curr_time_distance;

    for (int i = 0; i < n; i++) {
        curr_time_distance = user_time - ft[i].departure_time;
        if ((curr_time_distance > 0) &&
            (curr_time_distance < closest_time_distance)) {
                closest_index = i;
                closest_time_distance = curr_time_distance;
            }
    }


    return closest_index;
}