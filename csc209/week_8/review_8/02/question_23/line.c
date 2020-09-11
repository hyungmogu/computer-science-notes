
/* line.c (Chapter 15, page 364) */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "line.h"

#define MAX_LINE_LEN 60

struct node {
    char word[1];
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
  struct node *p = line;

  if (num_words > 0) {
      for (int i = 0; i < num_words; i++) {
          struct node *word;
          word = malloc(sizeof(struct node) + word_length);
          word->word[word_length] = '\0';

          if (p = NULL) {
              line = word;
          }

          while(p->next != NULL) {
              p = p->next;
          }

          p->next = word;
      }
  }
  line_len += strlen(word);
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