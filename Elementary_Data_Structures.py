# Array 
class Array:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        if 0 <= index <= len(self.data):
            self.data.insert(index, value)
        else:
            print("Index out of bounds.")

    def delete(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        else:
            print("Index out of bounds.")
            return None

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            print("Index out of bounds.")
            return None


# Matrix 
class Matrix:
    def __init__(self, rows, cols):
        self.data = [[0] * cols for _ in range(rows)]

    def insert(self, row, col, value):
        if 0 <= row < len(self.data) and 0 <= col < len(self.data[0]):
            self.data[row][col] = value
        else:
            print("Index error.")

    def access(self, row, col):
        if 0 <= row < len(self.data) and 0 <= col < len(self.data[0]):
            return self.data[row][col]
        else:
            print("Index error.")
            return None

    def display(self):
        for row in self.data:
            print(row)


# Stack 
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack is empty.")
            return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.stack) == 0


# Queue 
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            print("Queue is empty.")
            return None

    def is_empty(self):
        return len(self.queue) == 0


# Linked List 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            print("List is empty.")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            print("Element not found.")

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



#Usage demo
# Arrays
array = Array()
array.insert(0, 1)
array.insert(1, 2)
array.insert(2, 3)
print("Array after insertion:", array.data)
array.delete(1)
print("Array after deletion:", array.data)

# Matrices
matrix = Matrix(3, 3)
matrix.insert(0, 1, 5)
matrix.insert(1, 2, 8)
print("Matrix:")
matrix.display()

# Stacks
stack = Stack()
stack.push(33)
stack.push(20)
print("Stack top:", stack.peek())
stack.pop()
print("Stack after pop:", stack.stack)

# Queues
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print("Queue after enqueue:", queue.queue)
queue.dequeue()
print("Queue after dequeue:", queue.queue)

# Singly Linked List
sll = SinglyLinkedList()
sll.insert_at_beginning(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.traverse()
sll.delete(20)
sll.traverse()
