#include <stdio.h>

int sum(int (*f)(int), int start, int end);
int sample_function(int n);

int main(void) {
    int start = 1, end = 10, out;

    out = sum(sample_function, start, end);

    printf("%d\n", out);

    return 0;
}

int sum(int (*f)(int), int start, int end)
{
    int res = 0;
    for (int i = start; i <= end; i++) {
        res += (*f)(i);
    }

    return res;
}

int sample_function(int n) {
    return n + 1;
}