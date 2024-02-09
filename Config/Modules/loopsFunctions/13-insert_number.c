#include "lists.h"

/**
 * insert_node - Function inserts a number into a sorted singly linked list
 * @head: Pointer to the head of the linked list
 * @number: Number to be inserted
 *
 * Return: Address of the new node, or NULL if it failed
 * Author - Tafara-N
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = *head, *new;

    new = malloc(sizeof(listint_t));

    if (new == NULL)
        return (NULL);
    new->n = number;

    if (node == NULL || node->n >= number)
    {
        new->next = node;
        *head = new;
        return (new);
    }

    while (node && node->next && node->next->n < number)
        node = node->next;

    new->next = node->next;
    node->next = new;

    return (new);
}

