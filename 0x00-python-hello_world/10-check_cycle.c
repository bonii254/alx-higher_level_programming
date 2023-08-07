#include "lists.h"

/**
  * check_cycle - check if a list has a cycle.
  * @list: pointer to linked list.
  *
  * Return: 1 if have a cycle 0 if else.
  */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list->next->next;
	slow = list->next;

	if (list == NULL || list->next == NULL)
		return (0);
	while (fast && slow && fast->next)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
