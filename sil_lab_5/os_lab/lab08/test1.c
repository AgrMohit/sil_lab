#include <stdio.h>
#include <unistd.h>

int main() {
	int pid;
	pid = getpid();
	printf("Process id: %d\n", pid);
	return 0;
}

