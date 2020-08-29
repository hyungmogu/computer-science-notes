/* line.c (Chapter 15, page 364) */

#include <stdio.h>
#include <string.h>
#include "question23.h"

#define MAX_SIZE 60
#define MAX_LINE_LEN 60

struct word {
  char value[MAX_SIZE];
  struct word *next;
};


// char line[MAX_LINE_LEN+1];
struct word *line;
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

  strcpy(new_word->value, word);

  if (strlen(word) == MAX_SIZE) {
    new_word->value[MAX_SIZE - 1] = '\0';
  }

  if (num_words == 0) {
    line = new_word;
    line_len += strlen(word);
  } else {
    new_word->next = line;
    line = new_word;
    line_len += strlen(word) + 1; // +1 for space
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

  extra_spaces = MAX_LINE_LEN - line_len;
  for (i = 0; i < line_len; i++) {
    if (line[i] != ' ')
      putchar(line[i]);
    else {
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
  if (line_len > 0)
    puts(line);
}