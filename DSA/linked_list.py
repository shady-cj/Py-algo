# Constructing a singly linked list


# Defining the node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Defining a class for a singly linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        # Adds new node to the end of the linked list
        self.length += 1
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return self.tail
        current_node = self.tail
        current_node.next = new_node
        self.tail = new_node
        # Using this approach the appending to this linked list takes O(1)
        return self.tail

    def prepend(self, value):
        # Adds a new node to the beginning of the linked list
        self.length += 1
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return self.tail
        new_node.next = self.head
        self.head = new_node
        return self.head

    def size(self):
        # Returns the size of the linked list
        return self.length

    def print_list(self):
        # Prints the linked list
        linked_list = []
        if not self.head:
            return None
        current_node = self.head

        while current_node:
            linked_list.append(current_node.value)
            current_node = current_node.next
        return linked_list

    def remove(self, index):
        # Remove from the linked list or delete an element from the linked list
        if index > self.length:
            return None

        current_node = self.head
        prev_node = None
        pos = 0
        while current_node and pos < index:
            prev_node = current_node
            current_node = current_node.next
            pos += 1

        if self.head is None:
            return None
        self.length -= 1
        if self.head is not None and pos == 0:
            self.head = current_node.next
            if current_node.next is None:
                self.tail = None
            return self.head
        prev_node.next = current_node.next if current_node else None
        if current_node and current_node.next is None:
            self.tail = prev_node
        return prev_node.next

    def delete(self, value):
        # Deletes/removes an element from the linked list by the value
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.value == value:
                self.length -= 1
                if prev_node is None:
                    self.head = current_node.next
                    if current_node.next is None:
                        self.tail = None
                else:
                    prev_node.next = current_node.next
                    if current_node.next == None:
                        self.tail = prev_node
                return self.head

            prev_node = current_node
            current_node = current_node.next

        return None

    def insert(self, index, value):
        # Insert into the linked list at an index, using 0 as the starting index.
        self.length += 1
        new_node = Node(value)
        current_node = self.head
        prev_node = None
        pos = 0
        while current_node and pos < index:
            prev_node = current_node
            current_node = current_node.next
            pos += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return self.head
        elif self.head is not None and pos == 0:
            new_node.next = self.head
            self.head = new_node
            return self.head
        new_node.next = current_node
        prev_node.next = new_node
        if current_node == None:
            self.tail = new_node
        return new_node

    def reverse_list(self):
        # Reverse The Linked List
        if self.head is None:
            return None
        current_node = self.head
        next_node = None
        prev_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.tail = self.head
        self.head = prev_node
        return current_node


# 2 -> 3 -> 4 -> 4 -> 5

# cars = LinkedList()
# cars.append("Ford")
# print(cars.print_list())
# cars.remove(0)
# print(cars.print_list())
# print(cars.head, cars.tail)
# cars.insert(0, "Ford")
# print(cars.head, cars.tail, cars.print_list())
# cars.insert(0, "Benz")
# print(cars.head, cars.tail, cars.print_list())
# cars.append("Ford")
# cars.append("Mercedes Benz")
# cars.append("Aston Martin")
# cars.append("McLaurin")
# cars.append("Toyota")
# cars.append("Ferrari")
# print(cars.size())
# print(cars.print_list())
# cars.prepend("KIA")
# cars.prepend("Innoson")
# cars.prepend("Volkswagen")
# cars.prepend("SUV")
# print(cars.size())
# print(cars.print_list())
# cars.insert(0, "Chevrolet")
# cars.insert(1, "Ram")
# print(cars.print_list())
# cars.insert(5, "Honda")
# print(cars.print_list())
# print(cars.size())
# cars.insert(13, "Tesla")
# cars.append("Hyundai")
# print(cars.print_list())
# print(cars.size())
# cars.remove(14)
# print(cars.print_list())
# print(cars.size())
# cars.append("test")
# print(cars.print_list())
# cars.delete("test")
# print(cars.print_list())
# cars.append("Another test")
# print(cars.size())
# print(cars.print_list())
# cars.reverse_list()
# print()
# print("-------------------------")
# print(cars.print_list())
# cars.append("Final Test")
# print(cars.print_list())
# cars.reverse_list()
# print(cars.print_list())


# Defining a node for a doubly linked list


class DNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# Creating a doubly linked list


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        # Adds new node to the end of the linked list
        self.length += 1
        new_node = DNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return self.tail
        current_node = self.tail
        current_node.next = new_node
        new_node.prev = current_node
        self.tail = new_node
        # Using this approach the appending to this linked list takes O(1)
        return self.tail

    def prepend(self, value):
        # Adds a new node to the beginning of the linked list
        self.length += 1
        new_node = DNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return self.tail
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return self.head

    def size(self):
        # Returns the size of the linked list
        return self.length

    def print_list(self):
        # Prints the linked list
        linked_list = []
        if not self.head:
            return None
        current_node = self.head

        while current_node:
            linked_list.append(current_node.value)
            current_node = current_node.next
        return linked_list

    def print_reverse(self):
        # Prints the linked list in reverse
        reversed_linked_list = []
        if not self.tail:
            return None

        current_node = self.tail

        while current_node:
            reversed_linked_list.append(current_node.value)
            current_node = current_node.prev

        return reversed_linked_list

    def remove(self, index):
        # Remove from the linked list or delete an element from the linked list
        if index > self.length:
            return None
        current_node = self.head
        prev_node = None
        pos = 0
        while current_node and pos < index:
            prev_node = current_node
            current_node = current_node.next
            pos += 1

        if self.head is None:
            return None
        self.length -= 1
        if self.head is not None and pos == 0:
            if current_node.next is None:
                self.tail = None
            else:
                current_node.next.prev = None
            self.head = current_node.next

            return self.head
        prev_node.next = current_node.next if current_node else None
        if current_node and current_node.next is None:
            self.tail = prev_node
        elif current_node and current_node.next:
            current_node.next.prev = prev_node

        return prev_node.next

    def delete(self, value):
        # Deletes/removes an element from the linked list by the value
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.value == value:
                self.length -= 1
                if prev_node is None:
                    self.head = current_node.next
                    if current_node.next is None:
                        self.tail = None
                    else:
                        self.head.prev = None
                else:
                    prev_node.next = current_node.next
                    if current_node.next is None:
                        self.tail = prev_node
                    else:
                        current_node.next.prev = prev_node
                return self.head

            prev_node = current_node
            current_node = current_node.next

        return None

    def insert(self, index, value):
        # Insert into the linked list at an index, using 0 as the starting index.
        self.length += 1
        new_node = DNode(value)
        current_node = self.head
        prev_node = None
        pos = 0
        while current_node and pos < index:
            prev_node = current_node
            current_node = current_node.next
            pos += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return self.head
        elif self.head is not None and pos == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return self.head
        new_node.next = current_node
        prev_node.next = new_node
        new_node.prev = prev_node
        if current_node is None:
            self.tail = new_node
        else:
            current_node.prev = new_node
        return new_node


# 2 -> 3 -> 4 -> 4 -> 5

# cars = DoublyLinkedList()
# cars.append("Ford")
# print(cars.print_list())
# cars.remove(0)
# print(cars.print_list())
# print(cars.head, cars.tail)
# # cars.append("Ford")
# cars.append("Mercedes Benz")
# cars.append("Aston Martin")
# cars.append("McLaurin")
# cars.append("Toyota")
# cars.append("Ferrari")
# print(cars.size())
# print(cars.print_list())
# cars.prepend("KIA")
# cars.prepend("Innoson")
# cars.prepend("Volkswagen")
# cars.prepend("SUV")
# print(cars.size())
# print(cars.print_list())
# cars.insert(0, "Chevrolet")
# cars.insert(1, "Ram")
# print(cars.print_list())
# cars.insert(5, "Honda")
# print(cars.print_list())
# print(cars.size())
# cars.insert(13, "Tesla")
# cars.append("Hyundai")
# print(cars.print_list())
# print(cars.size())
# cars.remove(14)
# print(cars.print_list())
# print(cars.size())
# cars.append("test")
# print(cars.print_list())
# cars.delete("test")
# print(cars.print_list())
# cars.append("Another test")
# print(cars.size())
# print(cars.print_list())
# # cars.reverse_list()
# print()
# print("-------------------------")
# print(cars.print_list())
# cars.append("Final Test")
# print(cars.print_list())
# # cars.reverse_list()
# print(cars.print_list())
# print(cars.print_reverse())
