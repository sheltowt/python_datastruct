'''
search = O(n)
storage = O(n)
'''


class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

s = Stack()
print s.push("dog")
print s.push("cat")
print s.pop()

print s.size()

