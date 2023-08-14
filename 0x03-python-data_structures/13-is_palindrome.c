#include "lists.h"

/**
  * is_palindrome - check if linked list is palindrome.
  * @head: pointer to head node.
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *check;
	char *arry;
	int len = 0, i = 0, flag = 1, j;

	if (head == NULL || *head == NULL)
		return (0);

	temp = check = *head;
	while (temp != NULL)
	{
		len++;
		temp = temp->next;
	}

	arry = (char *) malloc(sizeof(int) * len);
	if (!arry)
		return (0);

	while(check != NULL)
	{
		arry[i] = check->n;
		check = check->next;
		i++;
	}

	for (j = 0; j < len / 2; j++)
	{
		if (arry[j] != arry[len - 1 - j])
		{
			flag = 0;
			break;
		}
	}
	free(arry);
	return (flag);
}
