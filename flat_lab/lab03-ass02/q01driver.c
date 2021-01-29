#include "q01desc.h"
#include <stdio.h>
#include <stdlib.h>

int main()
{
  char str[100];
  int i, flag;
  FILE *fptr;
  fptr = fopen("input-string.txt", "r");
  if (fptr == NULL)
  {
    printf("Error!");
    exit(1);
  }

  while (fscanf(fptr, "%s", str) != EOF)
  {
    i = 0;
    flag = 0;
    int cur_st = Initial_st;
    while (str[i] != '\0')
    {
      cur_st = Rules[cur_st][str[i] - '0'];
      i++;
    }
    for (i = 0; i < NoFst; i++)
    {
      if (cur_st == Final_st[i])
      {
        printf("String %8s -> ACCEPTED\n", str);
        flag = 1;
      }
    }
    if (flag == 0)
      printf("String %8s -> REJECTED\n", str);
  }
}