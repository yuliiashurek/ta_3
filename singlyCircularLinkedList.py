import numpy as np
import time


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SCLL:
    def __init__(self):
        self.tail = None
        self.head = None

    def insert_beginning(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        else:
            head = self.head
            while head.next != self.head:
                head = head.next
            head.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        else:
            head = self.head
            while head.next != self.head:
                head = head.next
            head.next = new_node
            new_node.next = self.head

    def insert_mid(self, val, size):
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            given_node = size // 2
            head = self.head
            for i in range(0, given_node):
                current = head
                head = head.next
            current.next = new_node
            new_node.next = head

    def delete_end(self):
        head = self.head
        if head is None:
            return
        if head.next is None:
            head = None
        second_last = head
        while second_last.next.next != self.head:
            second_last = second_last.next
        second_last.next = self.head

    def delete_beginning(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
            else:
                head = self.head
                while head.next != self.head:
                    head = head.next
                self.head = self.head.next
                head.next = self.head

    def delete_mid(self, size):
        if self.head is None:
            return
        else:
            mid = size // 2
            if self.head != self.tail:
                head = self.head
                current = None
                for i in range(0, mid):
                    current = head
                    head = head.next
                if current is not None:
                    current.next = head.next
                else:
                    self.head = self.tail = head.next
                    self.tail.next = self.head
            else:
                self.head = self.tail = None

    def find_index(self, val_to_find):
        current = self.head
        counter = 0
        while current is not None and current.next != self.head:
            if current.val == val_to_find:
                return counter
            counter += 1
            current = current.next
        return False


def rand_scll(start_point: int, end_point: int, num_of_el_in_sll: int):
    scll = SCLL()
    for _ in range(num_of_el_in_sll):
        random_el = np.random.randint(start_point, end_point)
        scll.insert_end(random_el)
    return scll


def display(self):
    head = self.head
    if head is not None:
        while True:
            print(head.val, end=" ")
            head = head.next
            if head == self.head:
                break
        print()
    else:
        print("The list is empty.")


num_of_el = 1000
singlyCircularLinkedList = rand_scll(1, 100, num_of_el)
print("\tSingly Linked List")
display(singlyCircularLinkedList)

start = time.time()

# print("\tAdding to the middle")
# for _ in range(1000):
#     num = np.random.randint(1, 100)
#     singlyCircularLinkedList.insert_mid(num, num_of_el)
#     num_of_el += 1

# print("\tAdding to the beginning")
# for _ in range(1000):
#     num = np.random.randint(1, 100)
#     singlyCircularLinkedList.insert_beginning(num)

# print("\tAdding to the end")
# for _ in range(1000):
#     num = np.random.randint(1, 100)
#     singlyCircularLinkedList.insert_end(num)

# ------------------------------------------------------

# print("\tDeleting from the middle")
# for _ in range(1000):
#     singlyCircularLinkedList.delete_mid(num_of_el)
#     num_of_el -= 1

# print("\tDeleting from the beginning")
# for _ in range(1000):
#     singlyCircularLinkedList.delete_beginning()

# print("\tDeleting from the end")
# for _ in range(1000):
#     singlyCircularLinkedList.delete_end()

# ------------------------------------------------------

# print("\tFind index")
# for _ in range(1000):
#     num = np.random.randint(101, 200)
#     singlyCircularLinkedList.find_index(num)

end = time.time()

print("Execution time of the program is ", end - start)
