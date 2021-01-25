#include <stdio.h>
#include <unistd.h>

int main()
{
  int i, num, pid;
  printf("Enter a number: ");
  scanf("%d", &num);
  pid = fork();

  if (pid == 0)
  {
    // Child Process - prime
    for (i = 2; i < num; i++)
    {
      if (num % i == 0)
      {
        printf("%d is not a prime number\n", num);
        break;
      }
    }
    if (i == num)
      printf("%d is a prime number\n", num);
  }
  else
  {
    // Parent process - even or odd
    if (num % 2 == 0)
      printf("%d is an even number\n", num);
    else
      printf("%d is an odd number\n", num);
  }
}
