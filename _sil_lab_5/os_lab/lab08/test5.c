#include <stdio.h>
#include <unistd.h>

int main() {
	int pid = fork();
	if (pid==0)
		printf("Parent Process\n");
	else
		printf("Child Process\n");
	return 0;
}


