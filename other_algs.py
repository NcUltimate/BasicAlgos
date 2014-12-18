############################
# DATA STRUCTURE: Union Find
# ~ Constructor initializes an empty union-find, which supports
# ~ two basic operations (unsurprisingly): Union, and find. This
# ~ data structure is renowned for its O(log*n) query time due to
# ~ path compression up to the root with every find operation. It is a
# ~ type of 'disjoint set' data structure, meaning it has a set of 
# ~ elements, each of which belong to a different set.
############################
class UnionFind:

	def __init__(self, nodes = []):
		self.parent = {}
		self.rank = {}
		for node in nodes:
			self.makeset(node)

	def find(self, x):
		if(self.parent[x] != x):
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x] 

	def union(self, x, y):
		xpar, ypar = self.find(x), self.find(y)
		rx, ry = self.rank[xpar], self.rank[ypar]
		
		if(rx > ry):
			self.parent[xpar] = ypar
		elif(rx < ry):
			self.parent[ypar] = xpar
		else:
			self.parent[ypar] = xpar
			self.rank[xpar] += 1

	def makeset(self, x):
		self.parent[x] = x
		self.rank[x] = 0

	def unions(self):
		sets = {}
		for key in self.parent:
			k = self.parent[key]
			if(k not in sets[k]):
				sets[k] = []
			sets[k].append(key)
		ret = []
		for s in sets:
			ret.append(sets[s])

		return ret
