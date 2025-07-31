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

    def search(self, key):
        """
        search fo tthr first node containing  data that matches the key 
        returns the node or None if not found
        Takes O(n)time
        """
        current = self.head
        while current:
            if current.data == key:
                return current.data
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        inserts a new node contaning data at index position 
        insertaion takes O(1) but finding the nodeat the insertion takes O(n)
        so overall takes O(n)
        """

        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        romeves data that matches the key
        returns the node or One of key doesnt exist 
        takes O(n) time
        """
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node
        return current


    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node

        return " -> ".join(nodes)

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
        adds new NODE CONTANING data in O(1)time
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

  





    



