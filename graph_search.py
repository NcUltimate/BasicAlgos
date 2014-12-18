############################
# ALGORITHM: Breadth-First Search (BFS)
# ~ Takes a Graph and a query item as input. If the
# ~ item is found in the graph through the BFS, then
# ~ it updates its result to that vertex. Otherwise,
# ~ result becomes 'None' to indicate the query item
# ~ was not found.
#
# IMPLEMENTATION
# ~ A BFS iteratively adds vertices to a queue by
# ~ adding all neighbors first, then popping the queue
# ~ until it is empty and all vertices have been visited.
############################
class BFS:
	def __init__(self, graph, key, value):
		self.key = key
		self.value = value
		self.result = self.algorithm(graph)

	def algorithm(self, g):
		visited = set()
		for vtx in g.V():
			if(vtx in visited): continue
			visited.add(vtx)
			queue = [vtx]
			while(queue):
				v = queue.pop(0)
				if(g.data[v][self.key] == self.value): return v
				for neigh in g.neighbors(v):
					if(neigh in visited): continue
					visited.add(neigh)
					queue.append(neigh)
		return None

############################
# ALGORITHM: Depth-First Search (DFS)
# ~ Takes a Graph and a query item as input. If the
# ~ item is found in the graph through the DFS, then
# ~ it updates its result to that vertex. Otherwise,
# ~ result becomes 'None' to indicate the query item
# ~ was not found.
#
# IMPLEMENTATION
# ~ A DFS recursively visits the children of each node
# ~ before checking the node itself for the search query.
# ~ In large unbounded graphs, it would be wise to limit
# ~ the DFS with a maximum depth to make it a Depth
# ~ Limited Search. This functionality is available here.
############################
class DFS:
	def __init__(self, graph, max_depth = -1):
		self.key = key
		self.value = value
		self.max_d = max_depth
		self.visited = set()
		self.result = self.algorithm(graph, max_depth)

	def algorithm(self, g):
		for vtx in g.V():
			if(vtx in self.visited): continue
			self.visited.add(vtx)
			res = self.dfs_subroutine(g, vtx, 0)
			if(res != None): return res
		return None

	def dfs_subroutine(self, g, v, depth):
		if(depth > self.max_d and self.max_d != -1): return None

		for neigh in g.neighbors(v):
			if(neigh in self.visited): continue
			self.visited.add(neigh)
			self.dfs_subroutine(g, neigh, depth+1)

		if(g.data[v][self.key] == self.value): 
			return v
		else:
			return None
