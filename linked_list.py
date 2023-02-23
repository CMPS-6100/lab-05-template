class Node:
    """ done. """
    def __init__(self, element):
        """
        Construct a Node

        Parameters
        ----------
        element : AnyType
            An element to be stored in a Linked List
        """
        self.element = element
        # Create two attributes, next and prev and initialize them
        # to be None
        # These are set when a None is added to a Linked List
        self.next = None
        self.prev = None

    def __str__(self):
        if self.next == None:
            return "[{}]".format(self.element)
        else:
            return "[{}]<->".format(self.element)

class LinkedList:
    def __init__(self):
        self.size = 0
        self.HEAD = None
        self.TAIL = None

    def is_empty(self):
        """ done. """
        return self.size == 0

    def __eq__(self, other):
        """ done. """
        if(self.size != other.size):
            return False
        self_node = self.HEAD
        other_node = other.HEAD
        for i in range(self.size):
            if(self_node.element != other_node.element):
                return False
            self_node = self_node.next
            other_node = other_node.next
        return True

    def __str__(self):
        """ done. """
        node = self.HEAD
        list_str = ""
        if self.is_empty():
            return list_str
        while True:
            # print each node
            list_str += str(node)
            # if we are at the tail, stop
            if node == self.TAIL:
                break
            # move to the next node
            node = node.next
        return list_str

    def append(self, element):
        """ done. """
        node = Node(element)
        if self.is_empty():
            self.HEAD = node
            self.TAIL = node
        else:
            node.prev = self.TAIL
            self.TAIL.next = node
            self.TAIL = node
        self.size += 1

    def prepend(self, element):
        # TO-DO
        # Implement this
        # Insert this element at the HEAD of the list
        pass

    def insert(self, element, index):
        """ done. """
        # Handle the special cases of 
        # inserting at index 0
        if(index == 0):
            self.prepend(element)
            return
        # or inserting after the tail
        if(index == self.size):
            self.append(element)
            return
        
        # otherwise, general case
        # Create the new node
        node = Node(element)
        # iterate to the node before the insertion position.
        # if we want to insert at index 3, we need a reference
        # to the node at index 2
        #  0          1          2          3       
        # [17]  <->  [19]  <->  [23]  <->  [31]
        #                        ⬆︎    ⬆︎
        #                     BEFORE   Insert-Position
        # for ease, use function iterate_to_position
        before = self.iterate_to_position(index-1)
        after = before.next
        # update the pointers.
        before.next = node
        after.prev = node
        node.prev = before
        node.next = after
        # increment the size
        self.size += 1

    def iterate_to_position(self, index):
        """ done. """
        # iterate to the node at the given index.
        # if we want a reference to the node at
        # index 2, we start at the HEAD and move
        # forward two spots from the HEAD
        #  0          1          2          3       
        # [17]  <->  [19]  <->  [23]  <->  [31]
        #                        ⬆︎  
        node = self.HEAD
        for i in range(index):
            node = node.next
        return node

    def contains(self, key):
        """ done. """
        # guard against an empty list
        if self.is_empty():
            return False
        node = self.HEAD
        while True:
            # check each element
            if node.element == key:
                return True
            # if we are at the tail, stop
            if node == self.TAIL:
                break
            # move to the next node
            node = node.next
        return False

    def get(self, index):
        # TO-DO
        # Implement this
        # return the element at index
        pass

    def remove_first(self):
        """ done. """
        if self.size == 0:
            return # empty list, do nothing
        if self.size == 1:
            self.HEAD = None
            self.TAIL = None
            self.size -= 1
            return
        # move head forward, remembering previous head
        prev_head = self.HEAD
        self.HEAD = self.HEAD.next
        # break pointers
        prev_head.next = None
        self.HEAD.prev = None
        # decrement size
        self.size -= 1

    def remove_last(self):
        # TO-DO
        # Implement this
        # remove the element at the TAIL of the list
        pass

    def remove(self, element):
        # TO-DO
        # Implement this
        # remove the first instance of this element from the list
        pass