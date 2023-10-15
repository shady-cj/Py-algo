# creating an heap data structure
# The main types of heaps are min heap and max heap


class MinHeap:
    def __init__(self):
        self.heap = [None]
        self.length = 0

    def insert(self, value):
        if self.length == 0:
            self.length += 1
            self.heap.append(value)
        else:
            self.length += 1
            self.heap.append(value)

            # After appending we compare with the parent nodes and heapify up if necessary
            pointer = self.length
            parent_pointer = pointer // 2
            while parent_pointer >= 1:
                pointer_el = self.heap[pointer]
                parent_pointer_el = self.heap[parent_pointer]
                if pointer_el < parent_pointer_el:
                    self.heap[pointer], self.heap[parent_pointer] = (
                        self.heap[parent_pointer],
                        self.heap[pointer],
                    )
                    pointer = parent_pointer
                    parent_pointer = parent_pointer // 2
                else:
                    break

    def remove(self):
        # In heaps you remove the root node
        if self.length == 0:
            return None
        root_node = self.heap[1]
        last_node = self.heap[self.length]
        self.heap[1], self.heap[self.length] = self.heap[self.length], self.heap[1]
        self.heap.remove(root_node)
        self.length -= 1
        pointer = 1
        child_pointer = pointer * 2
        while child_pointer <= self.length:
            neighbor_pointer = child_pointer + 1
            if (
                neighbor_pointer <= self.length
                and self.heap[neighbor_pointer] < self.heap[child_pointer]
                and self.heap[neighbor_pointer] < self.heap[pointer]
            ):
                self.heap[neighbor_pointer], self.heap[pointer] = (
                    self.heap[pointer],
                    self.heap[neighbor_pointer],
                )
                pointer = neighbor_pointer
                child_pointer = neighbor_pointer * 2
            elif any(
                [
                    neighbor_pointer <= self.length
                    and self.heap[child_pointer] < self.heap[neighbor_pointer]
                    and self.heap[child_pointer] < self.heap[pointer],
                    self.heap[child_pointer] < self.heap[pointer],
                ]
            ):
                self.heap[child_pointer], self.heap[pointer] = (
                    self.heap[pointer],
                    self.heap[child_pointer],
                )
                pointer = child_pointer
                child_pointer = child_pointer * 2
            else:
                break
        return root_node

    def sorted_array(self):
        # return a sorted array, (heap sort)
        array = []
        while self.length >= 1:
            array.append(self.remove())
        return array


min_heap = MinHeap()
array = [39, 18, 54, 14, 17, 8, 20, 19, 25, 52, 60]
for data in array:
    min_heap.insert(data)


print(min_heap.heap)
print(min_heap.sorted_array())


class MaxHeap:
    def __init__(self):
        self.heap = [None]
        self.length = 0

    def insert(self, value):
        if self.length == 0:
            self.length += 1
            self.heap.append(value)
        else:
            self.length += 1
            self.heap.append(value)

            # After appending we compare with the parent nodes and heapify up if necessary
            pointer = self.length
            parent_pointer = pointer // 2
            while parent_pointer >= 1:
                pointer_el = self.heap[pointer]
                parent_pointer_el = self.heap[parent_pointer]
                if pointer_el > parent_pointer_el:
                    self.heap[pointer], self.heap[parent_pointer] = (
                        self.heap[parent_pointer],
                        self.heap[pointer],
                    )
                    pointer = parent_pointer
                    parent_pointer = parent_pointer // 2
                else:
                    break

    def remove(self):
        # In heaps you remove the root node
        if self.length == 0:
            return None
        root_node = self.heap[1]
        last_node = self.heap[self.length]
        self.heap[1], self.heap[self.length] = self.heap[self.length], self.heap[1]
        self.heap.remove(root_node)
        self.length -= 1
        pointer = 1
        child_pointer = pointer * 2
        while child_pointer <= self.length:
            neighbor_pointer = child_pointer + 1
            if (
                neighbor_pointer <= self.length
                and self.heap[neighbor_pointer] > self.heap[child_pointer]
                and self.heap[neighbor_pointer] > self.heap[pointer]
            ):
                self.heap[neighbor_pointer], self.heap[pointer] = (
                    self.heap[pointer],
                    self.heap[neighbor_pointer],
                )
                pointer = neighbor_pointer
                child_pointer = neighbor_pointer * 2
            elif any(
                [
                    neighbor_pointer <= self.length
                    and self.heap[child_pointer] > self.heap[neighbor_pointer]
                    and self.heap[child_pointer] > self.heap[pointer],
                    self.heap[child_pointer] > self.heap[pointer],
                ]
            ):
                self.heap[child_pointer], self.heap[pointer] = (
                    self.heap[pointer],
                    self.heap[child_pointer],
                )
                pointer = child_pointer
                child_pointer = child_pointer * 2
            else:
                break
        return root_node

    def sorted_array(self):
        # return a sorted array, (heap sort)
        array = []
        while self.length >= 1:
            array.append(self.remove())
        return array


max_heap = MaxHeap()

for data in array:
    max_heap.insert(data)

print(max_heap.heap)
print(max_heap.sorted_array())
