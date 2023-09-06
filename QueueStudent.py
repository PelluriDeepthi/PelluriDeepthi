from collections import deque
class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")

    def size(self):
        return len(self.items)

queue = Queue()
student1 = Student(101,"John")
student2 = Student(102,"Jane")
queue.enqueue(student1)
queue.enqueue(student2)
print(queue.dequeue().name)
print(queue.peek().name)