


class Node:
	def __init__(self, val):
		self.l = None
		self.r = None
		self.val = val

# getRoot
# add
# _add
# find
# _find
# delete

class BinaryTree:
	def __init__(self):
		self.root = None

	def getRoot(self):
		return self.root

	def add(self, val):
		if self.root == None:
			self.root = Node(val)
		else:
			_add(val, self.root)

	def _add(self, val, node):
		if node.val == None:
			node.val = Node[val]
		elif val > node.val:
			_add(val, node.r)
		else:
			_add(val, node.l)

	def find(self):
		if(self.root != None):
			return self._find(val, self.root)
		else:
			return None

	def _find(self, val, node):
		if(val == node.val)
			return node
		elif (val > node.val and node.r != None):
			_find(val, node.r)
		else (val < node.val and node.l != None):
			_find(val, node.l)

	def delete(self)
		self.root = None








