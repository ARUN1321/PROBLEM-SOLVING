class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None
class llist:
    def __init__(self):
        self.head = None
    def append(self, Data):
        node = Node(Data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node
    def remove(self,Data):
        node = self.head
        if node is not None:
            if node.data == Data:
                self.head = node.next
                node = None
                return
        while node is not None:
            if node.data == Data:
                break
            prev = node
            node = node.next
        prev.next = node.next
        node = None
        if node==None:
            return "nill"
    def print(self):
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next
a = llist()
n = int(input())
for i in range(n):
    a.append(int(input()))
a.remove(4)
a.print()