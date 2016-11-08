# node
# has data
# has next node

# get_data
# get_next
# set_next

class Node:
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, node):
		self.next = node

# linked_list
# has a head

# insert
# size
# search
# delete

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		node = Node(data)
		node.set_next(self.head)
		self.head = node

	def size(self):
		count = 0
		current = self.head
		while current:
			count += 1
			current = current.get_next()
		return count

	def search(self, data):
		current = self.head
		while current:
			d = current.get_data()
			if d == data:
				return True
			current = current.get_next()
		return False		


	def delete(self, data):
		current = self.head
		previous = None
		while current:
			d = current.get_data()
			if d == data:
				if previous == None:
					self.head = current.get_next()
					return
				else:
					previous.set_next(current.get_next())
			current = current.get_next()

if __name__ == '__main__':
	
	l = LinkedList()
	l.insert("a")
	print l.size()

	l.insert("b")

	l.delete("a")

	print l.size()





