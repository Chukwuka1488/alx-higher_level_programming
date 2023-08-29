#!/usr/bin/python3
class Node:
    """Node class for a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node object

        Args:
            data (int): The data of the new node, must be an integer.
            next_node (Node): The next node in the list, must be a Node object
            or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node with validation

        Args:
            value (int): The new data of the node, must be an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node in the list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list with validation

        Args:
            value (Node): The new next node in the list, must be a Node object
            or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class"""

    def __init__(self):
        """Initialize a new SinglyLinkedList object"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list
        (increasing order)

        Args:
            value (int): The data of the new node to insert.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return a string representation of the SinglyLinkedList"""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
