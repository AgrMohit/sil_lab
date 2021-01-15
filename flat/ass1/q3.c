#include <stdio.h>

void input(int[], int);
void search(int *, int, int);

int main()
{
  int len, ar[25], el;

  printf("Enter number of items in the array: ");
  scanf("%d", &len);

  input(ar, len);

  printf("Enter element you want to search for: ");
  scanf("%d", &el);

  search(ar, len, el);
}

void input(int ar[], int len)
{
  int i;
  printf("Enter %d items:\n", len);

  for (i = 0; i < len; i++)
    scanf("%d", &ar[i]);
}

void search(int *ptr, int len, int el)
{
  int i;
  for (i = 0; i < len; i++)
    if (*(ptr + i) == el)
    {
      printf("Element found at index %d\n", i);
      return;
    }
  printf("Element not found\n");
}
