#include <stdio.h>
#include <string.h>
void toUpper(char *);

int main()
{
  char str[25];

  printf("enter a string: ");
  scanf("%[^\n]s", str);

  toUpper(str);

  printf("%s", str);
  return 0;
}

void toUpper(char *str)
{
  int i;
  for (i = 0; i < strlen(str); i++)
    if (*(str + i) >= 'a' && *(str + i) <= 'z')
      *(str + i) = *(str + i) + 32;
  printf("%s", str);
}
