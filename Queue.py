class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		super(Queue, self).__init__()
		self.items = []
		
	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.append(item)

	def peek(self):
		return self.items[0]

	def dequeue(self):
		value = self.items[0]
		self.items.remove(value)
		return value

	def size(self):
		return len(self.items)
