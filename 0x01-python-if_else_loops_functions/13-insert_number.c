#include "lists.h"

/**
  * insert_node -  inserts a number into a sorted singly linked list.
  * @head: pointer to head node.
  * @number: value of node.
  *
  * Return: pointer to head node.
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *prev, *temp;

	if (*head == NULL)
		return (NULL);
	temp = (listint_t *) malloc(sizeof(listint_t));
	if (!temp)
		return (NULL);
	temp->n = number;
	temp->next = NULL;

	prev = *head;
	curr = prev->next;
	if (prev->n >= number)
	{
		temp->next = prev;
		*head = temp;
		return (*head);
	}
	
	while(curr->n < number || curr->next != NULL)
	{
		prev = curr;
		curr = curr->next;
	}
	if (curr->next == NULL)
	{
		curr->next = temp;
		return(*head);
	}
	temp->next = prev->next;
	prev->next = temp;
	return (*head);
}
