/* planet.c (Chapter 13, page 304) */
/* Checks planet names */

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

#define NUM_PLANETS 9

bool my_strcmp(const char *arg, const char *planet);

int main(int argc, char *argv[])
{
  char *planets[] = {"mercury", "venus", "earth",
                     "mars", "jupiter", "saturn",
                     "uranus", "neptune", "pluto"};
  int i, j;

  for (i = 1; i < argc; i++) {
    for (j = 0; j < NUM_PLANETS; j++)
      if (my_strcmp(argv[i], planets[j])) {
        printf("%s is planet %d\n", argv[i], j + 1);
        break;
      }
    if (j == NUM_PLANETS)
      printf("%s is not a planet\n", argv[i]);
  }

  return 0;
}

bool my_strcmp(const char *s, const char *planet) {
    // turn all characters in arg to lower case
    int n = strlen(s);

    char sa[n+1], *p;

    strcpy(sa, s);

    for (p = sa; p < sa + n; p++) {
        *p = tolower(*p);
    }

    // if equal, return true
    if (strcmp(sa, planet) == 0) {
        return true;
    }

    // if not equal, return false
    return false;
}