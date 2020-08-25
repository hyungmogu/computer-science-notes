#include <stdio.h>
#include <stdlib.h>  /* exit */
#include <ctype.h>   /* isdigit */
#include <stdbool.h> /* C99+ only */

#define SIZE 50
#define STACK_SIZE 100

/* external variables */
double contents[STACK_SIZE] = {0};
int top = 0;

int evaluate_RPN_expression(const char *expression);
void make_empty(void);
bool is_empty(void);
bool is_full(void);
void push(char i);
char pop(void);
void stack_overflow(void);
void stack_underflow(void);

int main(void) {

    char c, expression[SIZE], *p;
    int result;


    while(true) {
        p = expression;
        printf("Enter an RPN expression: ");
        while ((c = getchar()) != '\n') {
            *p++ = c;
        }

        *p = '\0';

        result = evaluate_RPN_expression(expression);

        printf("Value of expression: %d\n", result);
    }
}

void make_empty(void) {
    top = 0;
}

bool is_empty(void) {
    return top == 0;
}

bool is_full(void) {
    return top == STACK_SIZE;
}

void push(char i) {

    if (is_full())
        stack_overflow();
    else
        contents[top++] = i;
}

char pop(void) {

    if (is_empty())
        stack_underflow();
    else
        return contents[--top];
}

void stack_overflow(void) {
    printf("\nExpression is too complex\n");
    exit(EXIT_FAILURE);
}

void stack_underflow(void) {
    printf("\nNot enough operands in expression\n");
    exit(EXIT_FAILURE);
}

int evaluate_RPN_expression(const char *expression) {
    double result;
    int op1, op2;

    while (*expression != '\0') {
        if (isdigit(*expression)) {
            push(*expression - '0'); // converts character to integer
        } else {
            if (*expression == '=') {
                result = pop();
                return result;
                break;
            }

            switch(*expression) {
                case '+':
                    op1 = pop();
                    op2 = pop();
                    push(op1 + op2);
                    break;
                case '-':
                    op1 = pop();
                    op2 = pop();
                    push(op1 - op2);
                    break;
                case '*':
                    push(pop() * pop());
                    break;
                case '/':
                    op1 = pop();
                    op2 = pop();
                    push(op1 / op2);
                    break;
                default:
                    exit(EXIT_FAILURE);
            }
        }
    }

    exit(EXIT_FAILURE);
}