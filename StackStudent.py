class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

stack = Stack()
student1 = Student(101,"John")
student2 = Student(102,"Jane")
stack.push(student1)
stack.push(student2)
print(stack.pop().name)
print(stack.peek().name)
#print(stack.items)