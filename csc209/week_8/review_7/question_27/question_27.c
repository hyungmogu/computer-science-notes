#include <stdio.h>

#define N 8

struct flight_times {
    int departure_time;
    int arrival_time;
};


int find_closest_departure_time(int user_time, const struct flight_times ft[]);

int main(void) {
    int user_time,
        hour,
        minute;

    struct flight_times ft[N] = {
        {480, 616}, {583, 712}, {679, 811}, {767, 900},
        {840, 968}, {945, 1075}, {1140, 1280}, {1305, 1438}
    };

    printf("Enter a 24-hour time: ");
    scanf("%d :%d", &hour, &minute);
    user_time = hour * 60 + minute;

    int index = find_closest_departure_time(user_time, ft, N);

    printf("Closest departure time is ");

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