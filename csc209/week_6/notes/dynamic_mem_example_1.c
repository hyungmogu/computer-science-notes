#include <stdio.h>
#include <stdlib.h>

int *set_i_heap() {
    int *j_pt = malloc(sizeof(int));
    *j_pt = 5;
    return j_pt;
}

int *set_i_static() {
    int i_pt = 5;
    return &i_pt;
}

int some_other_function() {
    int value = 123;
    return value;
}

int main() {
    int *p1 = set_i_heap();
    int *p2 = set_i_static();
    some_other_function(); // <- Notice how the value inside replaces value set by i_pt
    printf("but if I try to access i now via *pt I get %d\n", *p1); // <- value shouldn't change
    printf("but if I try to access i now via *pt I get %d\n", *p2); // <- value is different
    return 0;
}