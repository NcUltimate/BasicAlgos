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
		self.result = self.algorithm(graph, key, value)

	def algorithm(self, g, k, q):
		visited = set()
		for vtx in g.V():
			if(vtx in visited): continue
			visited.add(vtx)
			queue = [vtx]
			while(queue):
				v = queue.pop(0)
				if(g.data[v]['id'] == q): return v
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
# ~ A DFS iteratively adds vertices to a stack by
# ~ adding all descendants first, then popping the stack
# ~ until it is empty and all vertices have been visited.
############################
class DFS:
	pass
