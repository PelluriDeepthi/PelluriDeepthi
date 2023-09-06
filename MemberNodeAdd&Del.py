'''write a program to perform inset and delete operations on a queue containing members details as given the following definition of item node:
member no integer
member name string
age integer'''
class MemberNode:
    def __init__(self, member_no, member_name, age):
        self.member_no = member_no
        self.member_name = member_name
        self.age = age

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty.")

# Create an empty queue
member_queue = Queue()

# Inserting member details
member1 = MemberNode(1, "Alice", 25)
member2 = MemberNode(2, "Bob", 30)
member3 = MemberNode(3, "Carol", 28)

member_queue.enqueue(member1)
member_queue.enqueue(member2)
member_queue.enqueue(member3)

# Deleting member details (performing dequeue)
deleted_member = member_queue.dequeue()
if deleted_member:
    print(f"Deleted member: Member No. {deleted_member.member_no}, Name: {deleted_member.member_name}, Age: {deleted_member.age}")

# Print the remaining members in the queue
print("Remaining members in the queue:")
for member in member_queue.items:
    print(f"Member No. {member.member_no}, Name: {member.member_name}, Age: {member.age}")
