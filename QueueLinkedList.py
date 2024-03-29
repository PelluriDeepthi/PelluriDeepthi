class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from empty queue")

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
print(queue.dequeue())
print(queue.peek())
print(queue.size())
print(queue.is_empty())