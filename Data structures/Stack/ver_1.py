class Stack:
    def __init__(self):
        self.items = [] # not in the innit so that it is not accessed by user so that they do not change the elements
        # using append or something else

    def push(self, element):
        self.items.append(element) # adds an element to index 0 each time. each element
        # after the first append get pushed to its adjacent index

    def pop(self):
        print(f"the popped element is: {self.items.pop()}")

    def size(self):
        print(f"the size of the stack is: {len(self.items)}")

    def peek(self):
        print(f"the peeked element is: {self.items[-1]}")

    def is_empty(self):
        print(f"it is {len(self.items) == 0} that the stack is empty")

    def print_stack(self):
        print("the current elements in the stack")
        for i in self.items:
            print(str(i))



s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.print_stack()
s.pop()
s.print_stack()
s.peek()
s.is_empty()
s.pop()
s.pop()
s.pop()
s.is_empty()
s.size()