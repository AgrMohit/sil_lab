#include <stdio.h>

void printVars(int, int);
void swap(int *, int *);

int main()
{
  int num1, num2;

  printf("Enter 2 variables: ");
  scanf("%d %d", &num1, &num2);

  printf("Before swap:\n");
  printVars(num1, num2);

  swap(&num1, &num2);

  printf("After swap:\n");
  printVars(num1, num2);

  return 0;
}

void printVars(int n1, int n2)
{
  printf("num1 = %d\tnum2 = %d\n", n1, n2);
}

void swap(int *n1, int *n2)
{
  int temp;
  temp = *n1;
  *n1 = *n2;
  *n2 = temp;
}