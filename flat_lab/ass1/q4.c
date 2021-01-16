#include <stdio.h>
#include <string.h>

void printReverse(char *);

int main()
{
  char str[25];

  printf("Enter a string: ");
  scanf("%[^\n]%*c", str);

  printReverse(str);
}

void printReverse(char *ptr)
{
  int i, len;
  len = strlen(ptr);
  for (i = len; i >= 0; i--)
    printf("%c", *(ptr + i));
  printf("\n");
}