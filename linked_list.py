class Node:
    """
    an onject for storing a single node of a linked list.
    Models 2 attributes - data and link to the next node in the list.
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "< Node data: %s >" % self.data


class LinkedList:

    """
    Returns the number of the nodes in th list and return in O(n) time

    singly lnked list
    """

    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head 

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        adds new NODE CONTANING data 
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    



