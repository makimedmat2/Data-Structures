class FirstQueue:

	def __init__(self): 
		self.items = []

	def __str__(self): 
		return str(self.items)

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)


class SecondQueue:

	def __init__(self):
		self.items = []

	def __str__(self):
		return str(self.items)

	def isEmpty(self): 
		return self.items == []

	def enqueue(self, item):
		self.items.insert(len(self.items), item)

	def dequeue(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)
