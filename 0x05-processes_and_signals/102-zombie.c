#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Running an infinite while loop
 *
 * Return: Always 0.
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - Creating five zombie processes
 *
 * Return: Always zero
 */

int main(void)
{
	pid_t pid;
	char tally = 0;

	while (tally < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID:%d\n", pid);
			sleep(1);
			tally++;
		}
		else
			exit(0);
	}

	infinite_while();
	return (EXIT_SUCCESS);
}
