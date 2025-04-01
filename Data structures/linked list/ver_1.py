class Node:
    def __init__(self, value, next_node=None):      # correct😊
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):       # correct😊
        self.head = None

    def insert(self, new_node): # this is appending a node to the end       # wrong ❌
        if self.head is not None:       # if the head node points to another node

            current = self.head # current is being used to track which node we are in the linked list.
            # So we set it to the first element in the linked list
            while current.next_node is not None: # while the current node is not tracking the last node in the linked list
                # when would this self.head is not None be True if the linked list has elements i.e. which is the first
                # node that points to Node? Ans: The last element
                current = current.next_node
                # ⬆️current tracks (shallow copy, i.e becomes a linked copy to the node it is
                # tracking. if something happens to current then the same things happens to the node it is
                # tracking/copying) the next element in the linked list
            current.next_node = new_node    # when the while loop becomes true which is last element in the linked list make it point in to the new_node
        else: # is the head pointer points to nothing then make it point to new node
            self.head = new_node

    def print_linked_list(self):    # wrong❌
        # did not make an if in case the linked list is empty
        if self.head is None:
            print("Linked list has no nodes")

        current = self.head
        index = 0
        while current is not None:  # using current.next_node skips the last element because current which is
            # the last e;ement point to None so it skips hhe while loop
            # current works because the Node object does not equate to None
            print(f"Node at position {index}'s value: {current.value}")
            current = current.next_node
            index += 1


    def delete(self, old_node):
        #   wrong❌: nothing done for when the linked list is empty
        if self.head is None:
            print("Linked list has no nodes")

        #   wrong❌: nothing done for when the head pointer is the one to be eliminated
        if self.head == old_node:
            first_node = self.head # a copy of the oldnode is made
            self.head = first_node.next_node # the  head node points to the copy of it self
            first_node = None # first node then throws away the copy and takes on the value of None (
            # remember the first_node is just a variable name so it can be anython)

        current = self.head
        while current.next_node is not None: # correct ✅
            if current.next_node == old_node: # if the next node is one to be deleted
                to_be_deleted = current.next_node # node to be deleted
                after_to_be_deleted = to_be_deleted.next_node # the node after the one to be deleted
                current.next_node = after_to_be_deleted # the node before the one to be deleted points to the
                # after the node that is to be deleter
                to_be_deleted.next_node = None # the node to be delted points to nothing
            current = current.next_node

    def search(self, looking_for):  # correct ✅
        if self.head is None:
            print("Linked list has no nodes")

        current = self.head
        while current is not None:
            if current == looking_for:
                print(f"The node you are looking for has been found. Its value is : {current.value}")
                break
            current = current.next_node
        else: # the last element points to none and it is not the number we are looking for
            print("The node you are looking for is not here")


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
LL = LinkedList()
LL.insert(n1)
LL.insert(n2)
LL.insert(n3)
LL.delete(n2)
LL.search(n3)
LL.print_linked_list()
