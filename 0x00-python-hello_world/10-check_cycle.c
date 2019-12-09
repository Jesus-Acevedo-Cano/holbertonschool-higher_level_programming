#include "lists.h"
/**
 * check_cycle - Function to know if a linked list has a cycle
 * @list: pointer to list
 *
 * Return: 0 if has no cycle, 1 if has a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *listA = list, *listB = list;

	while (listA != NULL && listB != NULL && listB->next != NULL)
	{
		listA = listA->next;
		listB = listB->next->next;
		if (listA == listB)
			return (1);
	}
	return (0);
}
