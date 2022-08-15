class Queue:
	def __init__(self):
		self.queue = list()

	def add(self, data):
		if data not in self.queue:
			self.queue.insert(0, data)
			return True
		return False

	def pop(self):
		if len(self.queue)>0:
			return self.queue.pop()
		return "Queue is empty"

	def size(self):
		return len(self.queue)

a = Queue()
a.add("Apple")
a.add("Mango")
a.add("guava")
a.add("papaya")
print(a.pop())
print(a.size())
