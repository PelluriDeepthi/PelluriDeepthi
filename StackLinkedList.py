class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items)==0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from empty stack")

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
print(stack.pop())
print(stack.peek())
print(stack.size())
print(stack.is_empty())