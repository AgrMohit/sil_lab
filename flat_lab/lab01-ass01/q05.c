#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
  char *x[20];
  int i, n = 0;
  void sort(int n, char *x[]);
  printf("enter number of strings: ");
  scanf("%d", &n);

  for (i = 0; i < n; i++)
  {
    printf("enter string %d : ", i + 1);
    x[i] = (char *)malloc(20 * sizeof(char));
    scanf("%s", x[i]);
  }

  sort(n, x);

  printf("sorted list:  \n");
  for (i = 0; i < n; i++)
    printf("%s\n", x[i]);
}

void sort(int len, char *strar[])
{
  int i, j;
  char tempstr[20];
  for (i = 0; i < len - 1; i++)
    for (j = i + 1; j < len; j++)
      if (strcmp(strar[i], strar[j]) > 0)
      {
        strcpy(tempstr, strar[j]);
        strcpy(strar[j], strar[i]);
        strcpy(strar[i], tempstr);
      }
  return;
}