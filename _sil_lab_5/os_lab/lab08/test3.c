#include <stdio.h>
#include <unistd.h>

int main() {
	printf("Welcome!\n");
	fork();
	printf("Hello World!\n");
	return 0;
}

