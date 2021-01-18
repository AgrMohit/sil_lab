#include <stdio.h>
#include <unistd.h>

int main()
{
  int pid = fork();
  if (pid != 0)
  {
    printf("Process id: %d\n", getpid());
    printf("Child Process id: %d\n", pid);
    printf("Parent Process id: %d\n", getpid());
  }
}