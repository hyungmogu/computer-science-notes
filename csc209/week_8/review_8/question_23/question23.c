/* line.c (Chapter 15, page 364) */

#include <stdio.h>
#include <stdlib.h> // free, malloc
#include <string.h>
#include <stddef.h> // NULL
#include "question23.h"

#define MAX_SIZE 60
#define MAX_LINE_LEN 60

struct word {
  char value[MAX_SIZE];
  struct word *next;
};


// char line[MAX_LINE_LEN+1];
struct word *line, *cur;
int line_len = 0;
int num_words = 0;

void clear_line(void)
{
  struct word *to_be_removed;

  while (line != NULL) {
    to_be_removed = line;
    line = line->next;
    free(to_be_removed);
  }
  line_len = 0;
  num_words = 0;
}

void add_word(const char *word)
{
  struct word *new_word;
  new_word = malloc(sizeof(struct word));

  if (new_word == NULL) {
    printf("ERROR: Cannot allocate space for struct word");
    exit(1);
  }

  printf("%s\n", word);

  strcpy(new_word->value, word);

  printf("%s\n", new_word->value);

  if (strlen(word) == MAX_SIZE) {
    new_word->value[MAX_SIZE - 1] = '\0';
  }

  if (num_words == 0) {
    line = new_word;
    cur = new_word;
    line_len += strlen(word);
  } else {
    cur->next = new_word;
    cur = cur->next;
    printf("%lu\n", strlen(word));
    line_len += strlen(word) + 1; // +1 for space
  }

  // printf("%s\n", cur->value);
  printf("%d\n", line_len);
  // printf("%d", num_words);
  num_words++;
}

int space_remaining(void)
{
  return MAX_LINE_LEN - line_len;
}

void write_line(void)
{
  int extra_spaces, spaces_to_insert, i, j;

  struct word *p;
  extra_spaces = MAX_LINE_LEN - line_len;

  for (p = line; p != NULL; p = p->next) {
    printf("%s\n", p->value);

    if (num_words != 1) {
      spaces_to_insert = extra_spaces / (num_words - 1);
      for (j = 1; j <= spaces_to_insert + 1; j++)
        putchar(' ');
      extra_spaces -= spaces_to_insert;
      num_words--;
    }
  }
  putchar('\n');
}

void flush_line(void)
{
  struct word *p;

  if (line_len > 0) {
    for (p = line; p != NULL; p++) {
      printf("%s", p->value);
      if (p->next != NULL) {
        putchar(' ');
      }
    }
  }
}