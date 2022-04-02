import numpy as np
import time


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_end(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def insert_beginning(self, val):
        new_node = Node(val)
        if self.head.val is None:
            self.head = self.tail = new_node
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node

    def insert_mid(self, val, size):
        given_node = size // 2
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            temp = self.head
            current = None

            for i in range(0, given_node):
                current = temp
                temp = temp.next

            current.next = new_node
            new_node.next = temp

    def delete_end(self):
        head = self.head
        if head is None:
            return
        if head.next is None:
            head = None
        second_last = head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def delete_beginning(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
            else:
                self.head = self.head.next

    def delete_mid(self, size):
        head = self.head
        if head is None:
            return
        if head.next is None:
            head = None
        mid = size // 2
        while mid > 1:
            mid -= 1
            head = head.next
        head.next = head.next.next

    def find_index(self, val_to_find):
        current = self.head
        counter = 0
        while current is not None:
            if current.val == val_to_find:
                return counter
            counter += 1
            current = current.next
        return False


def rand_sll(start_point: int, end_point: int, num_of_el_in_sll: int):
    sll = SLL()
    for _ in range(num_of_el_in_sll):
        random_el = np.random.randint(start_point, end_point)
        sll.insert_end(random_el)
    return sll


def display(self):
    if self.head is not None:
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()
    else:
        print("The list is empty.")


num_of_el = 1000
singlyLinkedList = rand_sll(1, 100, num_of_el)
print("\tSingly Linked List")
display(singlyLinkedList)

start = time.time()

# print("\tAdding to the middle")
# for _ in range(1000):
#     num = np.random.randint(1, 100)
#     singlyLinkedList.insert_mid(num, num_of_el)
#     num_of_el += 1

# print("\tAdding to the beginning")
# for _ in range(1000):
#     num = np.random.randint(1, 100)
#     singlyLinkedList.insert_beginning(num)

# print("\tAdding to the end")
# for _ in range(1000):
#     num = np.random.randint(1, 100)
#     singlyLinkedList.insert_end(num)

# ------------------------------------------------------

# print("\tDeleting from the middle")
# for _ in range(1000):
#     singlyLinkedList.delete_mid(num_of_el)
#     num_of_el -= 1

# print("\tDeleting from the beginning")
# for _ in range(1000):
#     singlyLinkedList.delete_beginning()

# print("\tDeleting from the end")
# for _ in range(1000):
#     singlyLinkedList.delete_end()

# ------------------------------------------------------

# print("\tFind index")
# for _ in range(1000):
#     num = np.random.randint(101, 200)
#     singlyLinkedList.find_index(num)

end = time.time()

print("Execution time of the program is ", end - start)
