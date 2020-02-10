#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
/**
 **zombie - copy a strings
 *
 * @child_pid: is a pid
 * Return: On succes string.
 * On error.
 */

void zombie(__pid_t child_pid)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			printf("Zombie process created, PID:%d\n", getpid());
			exit(0);
		}
	}
}

/**
 **infinite_while - copy a strings
 *
 * Return: On succes string.
 * On error.
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/* betty style doc for function main goes there */
/**
 * main - Entry point
 *
 * Return: Always 0 (Success)
 */

int main(void)
{
	__pid_t child_pid = 0;

	zombie(child_pid);
	infinite_while();
	return (0);
}
