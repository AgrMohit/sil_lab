#include <stdio.h>

void input(int[], int);
void display(int[], int);
void sort(int *, int);

int main()
{
  int len, ar[25];

  printf("Enter number of items in the array: ");
  scanf("%d", &len);

  input(ar, len);

  printf("Before sort: \n");
  display(ar, len);

  sort(ar, len);

  printf("After sort: \n");
  display(ar, len);
}

void input(int ar[], int len)
{
  int i;
  printf("Enter %d items:\n", len);

  for (i = 0; i < len; i++)
    scanf("%d", &ar[i]);
}

void display(int ar[], int len)
{
  int i;
  for (i = 0; i < len; i++)
    printf("%d ", ar[i]);
  printf("\n");
}

void sort(int *ar, int len)
{
  int i, j, temp;

  for (i = 0; i < len; i++)
    for (j = i + 1; j < len; j++)
      if (*(ar + j) < *(ar + i))
      {
        temp = *(ar + i);
        *(ar + i) = *(ar + j);
        *(ar + j) = temp;
      }
}
