#id 
#adjacent

#add neighbor
#get connections
#get id
#get weight

class Vertex:
	def __init__(self, id):
		self.id = id
		self.adjacent = {}

	def add_neighbor(self, neighbor, weight):
		self.adjacent[neighbor] = weight

	def get_connections(self):
		return self.adjacent.keys()

	def get_id(self):
		return self.id

	def get_weight(self, neighbor):
		return self.adjacent[neighbor]





