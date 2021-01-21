#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void subStr(char *, char *);

int main()
{
  char s1[100], s2[100];
  printf("enter the mother string :\n");
  scanf("%s", s1);
  printf("enter the daughter string:\n");
  scanf("%s", s2);

  subStr(s1, s2);
}

void subStr(char *s1, char *s2)
{

  char s3[100];
  int i, m, n, j, k, flag = 0, count = 0;
  n = strlen(s1);
  m = strlen(s2);
  for (i = 0; i < (n - m) + 1; i++)
  {
    if (s1[i] == s2[0])
    {
      for (j = i, k = 0; j < m + i, k < m; j++, k++)
        s3[k] = s1[j];
      s3[m] = '\0';
      if (strcmp(s3, s2) == 0)
      {

        count++;
        flag = 1;
      }
    }
  }
  if (flag == 1)
  {
    printf("%s is substring of %s\n", s2, s1);
    printf("No of times :%d\n", count);
  }
  if (flag == 0)
    printf("%s is not a substring of %s \n", s2, s1);
}
