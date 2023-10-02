# Creating the Queue data structure (FIFO)

# Implementing features like
# enqueue()(0(1)), dequeue()(0(1)), peek()(0(1)), isEmpty()(0(1))

# The Queue data structure can be implemented using either an array or a linked list.


# Implementing stacks using arrays (Implementation using 2 stacks)
# Push operations uses 0(n) time complexity
# dequeue and peek operations uses O(1) time complexity


class QueueUsing2Stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.length = 0

    def enqueue(self, data):
        while len(self.stack1):
            popped_el = self.stack1.pop()
            self.stack2.append(popped_el)
        self.stack2.append(data)
        while len(self.stack2):
            popped_el = self.stack2.pop()
            self.stack1.append(popped_el)
        self.length += 1

    def dequeue(self):
        if self.length:
            self.length -= 1
            return self.stack1.pop()

    def peek(self):
        if self.length:
            return self.stack1[-1]

    def isEmpty(self):
        return not bool(self.length)


# cars = QueueUsing2Stacks()

# cars.enqueue("Ford")
# cars.enqueue("Benz")
# cars.enqueue("Aston Martin")
# print(cars.dequeue())
# print(cars.peek())
# print(cars.dequeue())
# print(cars.peek())
# print(cars.dequeue())
# print(cars.peek())


# Implementing Queues using Linked List all operations runs in O(1) time complexity


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueUsingLL:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        front_node = self.front
        self.front = front_node.next
        if self.front is None:
            self.back = None
        self.length -= 1
        return front_node.value

    def peek(self):
        if self.length:
            return self.front.value

    def isEmpty(self):
        return not bool(self.length)


cars = QueueUsingLL()

cars.enqueue("Ford")
cars.enqueue("Benz")
cars.enqueue("Aston Martin")
print(cars.dequeue())
print(cars.peek())
print(cars.dequeue())
print(cars.peek())
print(cars.dequeue())
print(cars.peek())
