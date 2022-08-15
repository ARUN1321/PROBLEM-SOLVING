class Node:
    # creating the storage space for data
    def __init__(self, data=None):
        self.data = data  # Assign data
        self.next = None  # initialize next as null


class LinkedList:
    # creating a head of the node
    def __init__(self):
        self.head = None

    # to insert data in the begining
    def Atbegining(self, newdata):
        newdata = Node(newdata)
        newdata.next = self.head
        self.head = newdata

    # inserting datas
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    # print the list
    def print(self):
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next


a = LinkedList()
a.append("mon")
a.append("Tue")
a.append("wed")
a.append("thu")
a.Atbegining("sun")
a.print()
