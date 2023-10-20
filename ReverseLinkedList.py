class Node:
    def __int__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to intialize head
    def __int__(self):
        self.head = None

    # Funtion to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

        # Function to insert a new node at the beginning
        def push(self, new_data):
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node

        # Utility function to print the LinkedList
        def printlist(self):
            temp = self.head
            while(temp):
                print(temp.data, end=" ")
                temp = temp.next

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("Given LinkedList")
llist.printlist()
llist.reverse()
print("\nReversed LinkedList")
llist.printlist()