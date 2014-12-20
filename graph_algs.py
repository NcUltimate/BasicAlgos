############################
# ALGORITHM: Bipartite
# ~ Takes a Graph as input. If the graph is bipartite, the
# ~ algorithm will successfully split it into two accessible
# ~ bipartitions. If not, the bipartitions will remain
# ~ empty, and is_bipartite will return False.
#
# IMPLEMENTATION:
# ~ Performs a Breadth-First Traversal, 2-coloring nodes
# ~ along the way. If any 2 adjacent nodes ever share the 
# ~ same color, the graph cannot be bipartite.
############################
class Bipartite:
	def __init__(self, graph):
		self.A, self.B = [], []
		self.algorithm(graph)

	def algorithm(self, g):
		marked, visited = {}, set()
		for vtx in g.V():
			if(vtx in visited): continue
			marked[vtx] = True
			visited.add(vtx)
			queue = [vtx]
			while(queue):
				v = queue.pop(0)
				for neigh in g.neighbors(v):
					# premature vertex marking sameness detection
					if(neigh in marked and marked[neigh] == marked[v]):
						return
					if(neigh in visited): continue
					marked[neigh] = not marked[v]
					visited.add(neigh)
					queue.append(neigh)

		# check that the endpoints of each
		# edge are not the same marking.
		for edge in g.E():
			edge = list(edge)
			m0 = marked[edge[0]]
			m1 = marked[edge[1]]
			if( m0 == m1): return

		# it is bipartite if the function reaches this point.
		# divide into A and B bipartitions
		for vertex in g.V():
			if(marked[vertex]):
				self.A.append(vertex)
			else:
				self.B.append(vertex)

	def partitions(self):
		return [self.A, self.B]

	def is_bipartite(self):
		return len(self.A)!=0 and len(self.B)!=0


############################
# ALGORITHM: Connected Components of a Graph
# ~ Takes a Graph as input, and determines its connectivity.
# ~ A graph is connected if there is a path from any node to
# ~ any other node in the graph.
#
# IMPLEMENTATION:
# ~ Use a union-find to union all nodes in the graph based
# ~ on the edges in the graph. Then look at the number of
# ~ unions to determine the connected components of the graph.
############################
class ConnectedComponents:

	def __init__(self, graph):
		self.comps = []
		self.union_find = UnionFind(graph.V())
		self.algorithm(graph)

	def algorithm(self, graph):
		for e in graph.E():
			self.union_find.union(e.v1, e.v2)
		self.comps = self.union_find.unions()

	def is_connected(self):
		return len(self.comps) == 1

	def components(self):
		return self.comps


############################
# ALGORITHM: Breadth-First Search (BFS)
# ~ Takes a Graph and a query item as input. If the
# ~ item is found in the graph through the BFS, then
# ~ it updates its result to that vertex. Otherwise,
# ~ result becomes 'None' to indicate the query item
# ~ was not found.
#
# IMPLEMENTATION:
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
# IMPLEMENTATION:
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

############################
# ALGORITHM: Spanning Tree
# ~ Takes a Graph as input, and returns a spanning tree
# ~ of the graph. A spanning tree is a minimal set of
# ~ connected edges such that every vertex in the graph
# ~ is an endpoint of at least one edge.
# 
# IMPLEMENTATION:
# ~ Perform a Breadth-First Traversal. Along the way, if a
# ~ Non-tree edge is encountered, remove it from the graph.
############################
class SpanningTree:

	def __init__(self, graph):
		self.tree = graph
		if(not graph.is_directed()):
			self.algorithm()

	def algorithm(self):
		visited = set()
		for vtx in self.tree.V():
			if(vtx in visited): continue
			visited.add(vtx)
			queue = [vtx]
			while(queue):
				v = queue.pop(0)
				visited.add(v)
				for neigh in self.tree.neighbors(v):
					if(neigh in visited): continue
					if(neigh in queue):
						self.tree.disconnect(v, neigh)
						continue
					queue.append(neigh)

	def spanning_tree(self):
		return self.tree

############################
# ALGORITHM: Cycle Detection
# ~ Takes a Graph as input, and returns the number of simple
# ~ cycles in the graph.
#
# IMPLEMENTATION:
# ~ Find a Spanning Tree of the graph. The number of edges
# ~ in the graph that aren't in the spanning tree (Non-tree
# ~ edges) is the number of cycles.
############################
class CycleDetection:

	def __init__(self, graph):
		self.cycles = 0
		self.algorithm(graph)

	def algorithm(self, g):
		g_edges = len(g.E)
		st = SpanningTree(g)
		self.cycles = g_edges- len(st.tree.E)

	def is_acyclic(self):
		return self.cycles == 0



