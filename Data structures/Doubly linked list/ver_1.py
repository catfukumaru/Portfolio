class Node:
    def __init__(self, value, prev_node = None, next_node = None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node



class DoublyLinkedList:
    def __init__(self):     # correct
        self.head = None
        self.tail = None

    def print_dl_list(self):
        current = self.head # get the first node

        index = 0
        while current is not None:
            print(f"Node at position {index}'s value: {current.value}")
            current = current.next_node
            index += 1

    def size(self):
        current = self.head  # get the first node

        total = 0
        while current is not None:
            current = current.next_node
            total += 1
        return total

    def insert_at_start(self, add_node): # wrong ❌: did not get how to swap the pointers
        # points to the old head
        add_node.next_node = self.head # the next pointer of the new node points to the head node which feels like it is going backwards
        add_node.prev_node = None # the new node's previous pointer points to nothing

        if self.head is not None: # if the list is not empty
            self.head.prev_node = add_node # give the og first node a previous node to the new node

        self.head = add_node # remember the that variables are just labels. head takes on the value of add_node

    def insert_at_end(self, add_node):

        add_node.next_node = None  # ✅

        if self.head is None: # wrong ❌: used tail instead of head beacuese i am addning an element to the end of
            # the list so i thought that wait the tail pointer had is what mattered. if the list is empty
            add_node.prev_node = None
            self.head = add_node
            return

        #loop through the linked list
        current = self.head

        while current.next_node:
            current = current.next_node

        # when at the end have current point to new node
        current.next_node = add_node
        add_node.prev_node = current


    def insert_before_node(self, ref_node, add_node):
        # Check if the list is empty
        if self.head is None:
            print("the list is empty")

        # Set the previous node of the add_node to the previous node of the reference node
        add_node.prev_node = ref_node.prev_node
        ref_node.prev_node = add_node # Set the previous node of the reference node to the add_node
        add_node.next_node = ref_node  # Set the next node of the add_node to the reference node

        if add_node.prev_node is not None: # if it is not the head
            add_node.prev_node.next_node = add_node # Link the previous node's next to the new node

        else:
            self.head = add_node # the head pointer points to the add_node


    def insert_after_node(self, ref_node, add_node):
        # Check if the list is empty
        if self.head is None:
            print("the list is empty")

        # add_node's next pointer points to the node that comes after ref_node
        add_node.next_node = ref_node.next_node
        # ref_node's next pointer points to add_node
        ref_node.next_node = add_node
        # add_node's previous pointer points to ref_node
        add_node.prev_node = ref_node

        if add_node.next_node is not None: # If the new node is not being inserted at the end of the list
            # the node after add_node previous pointer points to add_node
            add_node.next_node.prev_node = add_node

    def deleter_at_start(self):
        if self.head is None: # Check if the list is empty
            print("the list is empty")

        if self.head.next_node is None: # there is only one element in the list
            self.head = None # Set the head to None, effectively deleting the only element

        self.head = self.head.next_node # Move the head to the next node
        self.head.prev_node = None # Set the previous node of the new head to None

    def deleter_at_end(self):
        if self.head is None: # Check if the list is empty
            print("the list is empty")

        if self.head.next_node is None:  # there is only one element in the list
            self.head = None # Set the head to None, effectively deleting the only element

        current = self.head # Start from the head of the list
        while current.next_node is not None: # Traverse to the last node
            current = current.next_node

        current.prev_node.next_node = None # Set the next of the second last node to None, effectively removing the last node
        




# define a new list
double_list = DoublyLinkedList()

# insert a value at the beginning, like a stack because the first elemnt in is the last one that would be out if the linked list was a stack
double_list.insert_at_start(Node(90))
double_list.insert_at_start(Node(90))
double_list.insert_at_start(Node(90))
double_list.insert_at_start(Node(80))
double_list.insert_at_start(Node(70))

print('-' * 100)
print('After Insertion')
print('-' * 100)
double_list.print_dl_list()

    # def insert(self, add_node):
    #     # adds to the back of a list
    #     add_node.prev_node = self.head
    #
    #     if self.tail == None:   # if the doubly linked list is empty
    #         self.head = add_node
    #         self.tail = add_node
    #         add_node.next_node = None
    #     else:   # if the doubly linked list is not empty
    #         current = self.head
    #         while current.next_node is not None: # traverse to the end last element in the DLL
    #             current = current.next_node
    #         current.next = add_node
    #         add_node.prev_node = current