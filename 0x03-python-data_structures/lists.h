#ifndef lists_h_
#define lists_h_

#include <stdlib.h>

/**
* struct listint_s - singly
* @n: integer
* @next: next_node
* Description: singly ll
*/

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);

#endif
