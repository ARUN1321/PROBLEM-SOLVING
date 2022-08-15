class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.head = None

	def empty(self):
		if self.head == None:
			return True
		else:
			return False

	def push(self, data):
		if self.head == None:
			self.head = Node(data)
		else:
			newdata = Node(data)
			newdata.next = self.head
			self.head = newdata

	def pop(self):
		if self.empty():
			return "No data"
		else:
			pop = self.head
			self.head = self.head.next
			pop.next = None
			return pop.data

	def peek(self):
		if self.empty():
			return "No data"
		else:
			return self.head.data

	def print(self):
		datas = self.head
		if self.empty():
			return "No data"
		else:
			while(datas != None):
				print(datas.data)
				datas = datas.next
			return

a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.pop()
a.peek()
a.print()
