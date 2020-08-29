/* inventory.c (Chapter 16, page 391) */
/* Maintains a parts database (array version) */

#include <stdio.h>
#include <stdlib.h>
#include "readline.h"

#define NAME_LEN 25

struct part {
  int number;
  char name[NAME_LEN+1];
  int on_hand;
};

int compare_parts(const void * a, const void * b);
int find_part(int number, int num_parts, const struct part inventory[]);
void insert(int *num_parts, int *max_parts, struct part inventory[]);
void search(int num_parts, const struct part inventory[]);
void update(int num_parts, struct part inventory[]);
void print(int num_parts, const struct part inventory[]);

/**********************************************************
 * main: Prompts the user to enter an operation code,     *
 *       then calls a function to perform the requested   *
 *       action. Repeats until the user enters the        *
 *       command 'q'. Prints an error message if the user *
 *       enters an illegal code.                          *
 **********************************************************/
int main(void)
{
  char code;
  int max_parts = 10;

  struct part *inventory = malloc(max_parts * sizeof(struct part));
  int num_parts = 0;   /* number of parts currently stored */

  for (;;) {
    printf("Enter operation code: ");
    scanf(" %c", &code);
    while (getchar() != '\n')   /* skips to end of line */
      ;
    switch (code) {
      case 'i':
        insert(&num_parts, &max_parts, inventory);
        break;
      case 's':
        search(num_parts, inventory);
        break;
      case 'u':
        update(num_parts, inventory);
        break;
      case 'p':
        print(num_parts, inventory);
        break;
      case 'q':
        qsort(inventory, num_parts, sizeof(inventory[0]), compare_parts);
        free(inventory);
        return 0;
      default:  printf("Illegal code\n");
    }
    printf("\n");
  }
}

int compare_parts(const void * a, const void * b) {

}

/**********************************************************
 * find_part: Looks up a part number in the inventory     *
 *            array. Returns the array index if the part  *
 *            number is found; otherwise, returns -1.     *
 **********************************************************/
int find_part(int number, int num_parts, const struct part inventory[])
{
  int i;

  for (i = 0; i < num_parts; i++)
    if (inventory[i].number == number)
      return i;
  return -1;
}

/**********************************************************
 * insert: Prompts the user for information about a new   *
 *         part and then inserts the part into the        *
 *         database. Prints an error message and returns  *
 *         prematurely if the part already exists or the  *
 *         database is full.                              *
 **********************************************************/
void insert(int *num_parts, int *max_parts, struct part inventory[])
{
  int part_number, i, j;

  if (*num_parts == *max_parts) {
    *max_parts = *max_parts * 2;
    inventory = realloc(inventory, *max_parts * sizeof(inventory[0]));
  }

  printf("Enter part number: ");
  scanf("%d", &part_number);
  if (find_part(part_number, *num_parts, inventory) >= 0) {
    printf("Part already exists.\n");
    return;
  }

  for (i = 0; i < *num_parts; i++) {
    if (part_number < inventory[i].number) {
      break;
    }
  }

  for (j = *num_parts; j > i; j--) {
    inventory[j] = inventory[j-1];
  }

  inventory[i].number = part_number;
  printf("Enter part name: ");
  read_line(inventory[i].name, NAME_LEN);
  printf("Enter quantity on hand: ");
  scanf("%d", &inventory[i].on_hand);
  *num_parts += 1;
}

/**********************************************************
 * search: Prompts the user to enter a part number, then  *
 *         looks up the part in the database. If the part *
 *         exists, prints the name and quantity on hand;  *
 *         if not, prints an error message.               *
 **********************************************************/
void search(int num_parts, const struct part inventory[])
{
  int i, number;

  printf("Enter part number: ");
  scanf("%d", &number);
  i = find_part(number, num_parts, inventory);
  if (i >= 0) {
    printf("Part name: %s\n", inventory[i].name);
    printf("Quantity on hand: %d\n", inventory[i].on_hand);
  } else
    printf("Part not found.\n");
}

/**********************************************************
 * update: Prompts the user to enter a part number.       *
 *         Prints an error message if the part doesn't    *
 *         exist; otherwise, prompts the user to enter    *
 *         change in quantity on hand and updates the     *
 *         database.                                      *
 **********************************************************/
void update(int num_parts, struct part inventory[])
{
  int i, number, change;

  printf("Enter part number: ");
  scanf("%d", &number);
  i = find_part(number, num_parts, inventory);
  if (i >= 0) {
    printf("Enter change in quantity on hand: ");
    scanf("%d", &change);
    inventory[i].on_hand += change;
  } else
    printf("Part not found.\n");
}

/**********************************************************
 * print: Prints a listing of all parts in the database,  *
 *        showing the part number, part name, and         *
 *        quantity on hand. Parts are printed in the      *
 *        order in which they were entered into the       *
 *        database.                                       *
 **********************************************************/
void print(int num_parts, const struct part inventory[])
{
  int i;

  printf("Part Number   Part Name                  "
         "Quantity on Hand\n");
  for (i = 0; i < num_parts; i++)
    printf("%7d       %-25s%11d\n", inventory[i].number,
           inventory[i].name, inventory[i].on_hand);
}