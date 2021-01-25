#include <stdio.h>
#include <unistd.h>

int main() {
	int pid = fork();
	if(pid==0) {
		printf("Child Process ID: %d\n", getpid());
		printf("Child's Prent Process ID: %d\n" getppid());
	}
	else if (pid<0)
		printf("Unable to create child process\n");
	


