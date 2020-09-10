#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <stdio.h>

#define INTSIZE 32
#define N 4

typedef struct bits {
    unsigned int field[N];
} Bitarray;

int setzero(Bitarray *b) {
    return (memset(b, 0, sizeof(Bitarray)) == NULL);
}

void set(unsigned int value, Bitarray *b) {
    int index = value / INTSIZE;
    b->field[index] |= 1 << (value % INTSIZE);
}


void unset(unsigned int value, Bitarray *b) {
    int index = value / INTSIZE;
    b->field[index] &= ~(1 << (value % INTSIZE));
}

int ifset(unsigned int value, Bitarray *b) {
    int index = value / INTSIZE;
    return (1 << (value % INTSIZE) & b->field[index]);
}


int main () {
    Bitarray a1;
    setzero(&a1);

    // Add 1, 16, 32, 65 to the set
    set(1, &a1);
    set(16, &a1);
    set(32, &a1);
    set(65, &a1);

    // expecting: [0x00010002, 0x00000001, 0x000000010, 0]
    printf("%x %x %x %x\n",
        a1.field[0], a1.field[1], a1.field[2], a1.field[3]);
}
