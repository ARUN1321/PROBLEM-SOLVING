class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode
    
    def print(self):
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next

    def maxsum(self):
        first = self.head
        last = self.head
        