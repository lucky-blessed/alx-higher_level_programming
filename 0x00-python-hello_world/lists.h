#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/**
 * struct listint_s - singly linked list
 * @n: Integer
 * @next: Pointer to the next node
 *
 * Description: Singly linked list node structure 
 * for Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listiint_s;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(lisint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *lsit);

#endif /* LISTS_H */
