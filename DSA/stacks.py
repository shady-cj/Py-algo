# Creating the Stack data structure (LIFO)

# Implementing features like
# push()(0(1)), pop()(0(1)), peek()(0(1)), isEmpty()(0(1))

# The Stack data structure can be implemented using either an array or a linked list.


# Implementing stacks using arrays


class StackUsingArrays:
    def __init__(self):
        self.stack = []
        self.length = 0

    def pop(self):
        # removing an elementing from the top of the stack and returning it
        if self.length:
            topElement = self.stack.pop()
            self.length -= 1
            return topElement
        return None

    def push(self, data):
        # pushing data to the top of the stack
        self.stack.append(data)
        self.length += 1

    def peek(self):
        # checking and returning the data at the top of the stack without removing it
        if self.length:
            return self.stack[-1]
        return None

    def isEmpty(self):
        # Check whether the stack is empty
        return not bool(self.length)


# stack = StackUsingArrays()
# stack.push("test")
# stack.push("2")
# stack.push("data 2")
# stack.push("tester")

# print(stack.peek())
# print(stack.pop())
# print(stack.peek())


# Creating stacks Using linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackUsingLL:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        return new_node.value

    def pop(self):
        if self.length == 0:
            return None

        popped_node = self.top
        next_node = popped_node.next
        if next_node is None:
            self.bottom = None
        self.top = next_node
        self.length -= 1
        return popped_node.value

    def peek(self):
        if self.top:
            return self.top.value

    def isEmpty(self):
        return not bool(self.length)


stack = StackUsingLL()
stack.push("test")
stack.push("2")
stack.push("data 2")
stack.push("tester")

print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.isEmpty())
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.peek())
