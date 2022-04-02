class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        if self.tail is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def get_el(self):
        head = self.head
        if head is None:
            return
        element = self.head.val
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        return element

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def display(self):
        print("queue:", end=" ")
        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next


queue = Queue()
queue.add(4)
queue.add(5)
queue.add(6)
queue.add(7)
# 4 -> 5 -> 6 -> 7 -> None
queue.display()
print("\nqueue is empty:", queue.is_empty())

# get elements from the queue (print the element and remove it from the queue)
print("\n\telement removed from the queue: ", queue.get_el())
queue.display()
print("\n\telement removed from the queue: ", queue.get_el())
queue.display()
print("\n\telement removed from the queue: ", queue.get_el())
queue.display()
print("\n\telement removed from the queue: ", queue.get_el())
queue.display()

print()
print("\nqueue is empty:", queue.is_empty())
