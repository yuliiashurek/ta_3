import numpy as np
import time


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_mid(self, val, size):
        new_node = Node(val)
        given_node = size // 2
        if self.head is None:
            self.head = self.tail = new_node
            self.head.previous = self.tail.next = None
        else:
            current = self.head
            for i in range(0, given_node):
                current = current.next
            temp = current.next
            temp.previous = current

            current.next = new_node
            new_node.previous = current
            new_node.next = temp
            temp.previous = new_node

    def insert_beginning(self, val):
        new_node = Node(val)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_end(self, val):
        new_node = Node(val)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def delete_beginning(self):
        head = self.head
        if head is None:
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    def delete_end(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                second_last = self.head
                while second_last.next.next is not None:
                    second_last = second_last.next
                second_last.next = None

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
        head.next.prev = head

    def find_index(self, val_to_find):
        current = self.head
        counter = 0
        while current is not None:
            if current.val == val_to_find:
                return counter
            counter += 1
            current = current.next
        return False


def rand_dll(start_point: int, end_point: int, num_of_el_in_sll: int):
    dll = DLL()
    for _ in range(num_of_el_in_sll):
        random_el = np.random.randint(start_point, end_point)
        dll.insert_end(random_el)
    return dll


def display(self):
    if self.head is not None:
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()
    else:
        print("The list is empty.")


num_of_el = 1010
doublyLinkedList = rand_dll(1, 100, num_of_el)
print("\tDoubly Linked List")
display(doublyLinkedList)

start = time.time()

# print("\tAdding to the middle")
# for _ in range(1000):
#     num = np.random.randint(1, 100)
#     doublyLinkedList.insert_mid(num, num_of_el)
#     num_of_el += 1

# print("\tAdding to the beginning")
# for _ in range(1000):
#     num = np.random.randint(1, 100)
#     doublyLinkedList.insert_beginning(num)

# print("\tAdding to the end")
# for _ in range(1000):
#     num = np.random.randint(1, 100)
#     doublyLinkedList.insert_end(num)

# ------------------------------------------------------

# print("\tDeleting from the middle")
# for _ in range(1000):
#     doublyLinkedList.delete_mid(num_of_el)
#     num_of_el -= 1

# print("\tDeleting from the beginning")
# for _ in range(1000):
#     doublyLinkedList.delete_beginning()

# print("\tDeleting from the end")
# for _ in range(1000):
#     doublyLinkedList.delete_end()
#     display(doublyLinkedList)

# ------------------------------------------------------
#
# print("\tFind index")
# for _ in range(1000):
#     num = np.random.randint(101, 200)
#     doublyLinkedList.find_index(num)


end = time.time()

print("Execution time of the program is ", end - start)
