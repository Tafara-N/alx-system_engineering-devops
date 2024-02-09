#!/usr/bin/python3

"""
A class Node that defines a node of a singly linked list
"""


class Node:
    """
    Node of a singly-linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initializing a new Node

        Args:
            data (int): New Node's data
            next_node (Node): New Node's next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Gets or sets the data of the next Node
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Gets or sets the next_node of the Node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A singly-linked list
    """

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node to the Singly-linked list

        The node is inserted into the list in the correct
        numerical order position

        Args:
            value (Node): The new Node to insert.
        """
        current = Node(value)
        if self.__head is None:
            current.next_node = None
            self.__head = current
        elif self.__head.data > value:
            current.next_node = self.__head
            self.__head = current
        else:
            tmp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            current.next_node = temp.next_node
            temp.next_node = current

    def __str__(self):
        """
        The print() representation of a Singly-linked list
        """
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
