
/* line.c (Chapter 15, page 364) */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "line.h"

#define MAX_LINE_LEN 60

struct node {
    char word[MAX_LINE_LEN];
    struct node *next;
};

struct node *line = NULL;

int line_len = 0;
int num_words = 0;

void clear_line(void)
{
  struct node *p = line, *temp;

  while (p != NULL) {
      temp = p;
      p = p->next;
      free(temp);
  }
  line_len = 0;
  num_words = 0;
}

void add_word(const char *word)
{
  int word_length = strlen(word);
  struct node *p = line, *n;

  n = malloc(sizeof(struct node) + word_length);
  strcpy(n->word, word);

  if (p == NULL) {
      line = n;
      return;
  }

  while(p->next != NULL) {
      p = p->next;
  }

  p->next = n;

  line_len += strlen(n->word);

  if (num_words > 0) {
      line_len += 1 ;
  }

  num_words++;
}

int space_remaining(void)
{
  return MAX_LINE_LEN - line_len;
}

void write_line(void)
{
  int extra_spaces, spaces_to_insert, i, j;
  struct node *p;

  extra_spaces = MAX_LINE_LEN - line_len;
  for (p = line; p != NULL && num_words > 0; p = p->next) {
    printf("%s", p->word);

    if (num_words > 1) {
        spaces_to_insert = extra_spaces / (num_words - 1);
        for (j = 1; j <= spaces_to_insert + 1; j++)
            putchar(' ');
        extra_spaces -= spaces_to_insert;
    }
    num_words--;
  }
  putchar('\n');
}

void flush_line(void)
{
    struct node *p;

  if (line_len > 0)
    for (p = line; p != NULL; p = p->next) {
        printf("%s", p->word);
        if (p->next != NULL) {
            putchar(' ');
        }
    }
}