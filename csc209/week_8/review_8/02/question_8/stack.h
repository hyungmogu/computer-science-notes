#include <stdbool.h>

#ifndef STACK_H
#define STACK_H

void make_empty(void);
bool is_empty(void);
bool push(int i);
int pop(void);

#endif