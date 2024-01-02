#include "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: list that is going to be checked
 * Return:0 or 1 if successful or not
 */
int check_cycle(listint_t *list)
{
listint_t *turtle = list;
	listint_t *hare = list;

	while (turtle && hare && hare->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;

		if (turtle == hare)
			return (1);
	}

	return (0);
}
