#include <stdio.h>
#include <unistd.h>

int main()
{
  int i, pid;
  pid = fork();

  if (pid == 0)
  {
    // Child Process
    sleep(1);
    printf("Child starts\n");
    for (i = 1; i <= 10; i++)
      printf("%d ", i);
    printf("\nChild ends\n");
  }
  else
  {
    // Parent process
    printf("Parent starts\n");
    for (i = 1; i <= 10; i++)
      printf("%d ", i);
    printf("\nParent ends\n");
  }
}