#include <stdio.h>
#include <unistd.h>

int main()
{
  int i, pid;
  pid = fork();

  if (pid == 0)
  {
    // Child Process
    printf("Child starts\n");
    sleep(2);
    for (i = 1; i <= 10; i++)
      printf("%d ", i);
    printf("\nChild ends\n");
  }
  else
  {
    // Parent process
    printf("Parent starts\n");
    sleep(1);
    for (i = 1; i <= 10; i++)
      printf("%d ", i);
    printf("\nParent ends\n");
  }
}