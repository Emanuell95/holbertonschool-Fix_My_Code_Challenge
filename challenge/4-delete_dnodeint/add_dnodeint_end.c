#include <stdlib.h>
#include "lists.h"

/**
 * add_dnodeint_end - Add a node at the end of a dlistint_t list
 * @head: A pointer to the head of the list
 * @n: The integer to store in the new node
 *
 * Return: A pointer to the new node, or NULL on failure
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new, *last;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;
	new->prev = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	last = *head;
	while (last->next != NULL)
		last = last->next;

	last->next = new;
	new->prev = last;

	return (new);
}
