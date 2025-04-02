class Queue:
    def __init__(self):
        self.items = []


    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        self.items.pop(0) # removes the first element in a list

    def peek(self):
        print(f"the peeked element is: {self.items[0]}")

    def is_empty(self):
        print(f"it is {len(self.items) == 0} that the queue is empty")

    def size(self):
        print(f"the size of the queue is: {len(self.items)}")

    def print_queue(self):
        index = 0
        for i in self.items:
            print(f"the element in index {index} is {i}")
            index += 1

s = Queue()
s.enqueue(2)
s.enqueue(1)
s.enqueue(2)
s.enqueue(2)
s.print_queue()
s.dequeue()
print("\n\n after a dequeue\n") # 1,2,2
s.print_queue()
s.peek() # 1
s.is_empty() # False
s.dequeue() # 2,2
s.dequeue() # 2
s.dequeue() # 0
s.is_empty() # True
s.size() # 0