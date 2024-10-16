class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow!")
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow!")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) >= self.capacity

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()

    def display(self):
        print("Stack contents:", self.stack if self.stack else "Stack is empty!")

    def __iter__(self):
        return reversed(self.stack)  # Allows iteration from top to bottom


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow!")
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow!")
        return self.queue.pop(0)

    def front_element(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.capacity

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue.clear()

    def display(self):
        print("Queue contents:", self.queue if self.queue else "Queue is empty!")

    def __iter__(self):
        return iter(self.queue)  # Allows iteration from front to rear


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        if not self.head:
            print("Linked list is empty!")
            return
        current = self.head
        contents = []
        while current:
            contents.append(current.data)
            current = current.next
        print("Linked list contents:", " -> ".join(map(str, contents)) + " -> None")

    def clear(self):
        self.head = None
        print("Linked list cleared!")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


# Example usage:

# Stack operations
stack = Stack(5)
stack.push(10)
stack.push(20)
stack.display()  # Display stack contents
print("Popped from stack:", stack.pop())  # Output: 20
stack.display()  # Display stack contents after pop

# Iterate through stack
print("Iterating through stack:")
for item in stack:
    print(item)

stack.clear()    # Clear the stack
stack.display()  # Should indicate stack is empty

# Queue operations
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.display()  # Display queue contents
print("Dequeued from queue:", queue.dequeue())  # Output: 10
queue.display()  # Display queue contents after dequeue

# Iterate through queue
print("Iterating through queue:")
for item in queue:
    print(item)

queue.clear()    # Clear the queue
queue.display()  # Should indicate queue is empty

# Singly Linked List operations
linked_list = SinglyLinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.display()  # Output: 10 -> 20 -> None

# Reverse and display linked list
linked_list.reverse()
linked_list.display()  # Output: 20 -> 10 -> None

# Iterate through linked list
print("Iterating through linked list:")
for item in linked_list:
    print(item)

linked_list.clear()    # Clear the linked list
linked_list.display()  # Should indicate linked list is empty
