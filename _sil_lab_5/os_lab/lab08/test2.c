#include <stdio.h>
#include <unistd.h>

int main() {
	int pid;
	pid = getppid();
	printf("Parent Process id: %d\n", pid);
	return 0;
}

