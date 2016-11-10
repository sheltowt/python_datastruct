
class Node:
	def __init__(self, val):
		self.l = None
		self.r = None
		self.val = val

class BinaryTree:
	def __init__(self):
		self.root = None

	def add(val):
		if self.root == None:
			self.root = Node(val)
		else:
			_add(self.root, val)

	def _add(self, node, val):
		if val < node.val:
			if node.l = None:
				node.l = Node(val)
			else:
				self._add(node.l, val)
		else:
			if node.r = None:
				node.r = None(val)
			else:
				self._add(node.r, val)

	def find(self, val):
		if(self.root != None):
			return self._find(self.root, val)
		else:
			return None

	def _find(self, node, val):
		if(node == val):
			return node
		elif(val < node.v and node.l != None):
			self._find(self, node, val)
		elif(val > node.v and node.r != None):
			self._find(self, node, val)

	def delete(self):
		self.root = None



