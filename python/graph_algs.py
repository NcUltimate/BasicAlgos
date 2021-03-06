from other_algs import UnionFind
from heap import MinHeap
from graph import Graph

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
		for edge in g.E:
			edge = list(edge)
			m0 = marked[edge.v1]
			m1 = marked[edge.v2]
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
		for e in graph.E:
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
	def __init__(self, graph, key, value, max_depth = -1):
		self.key = key
		self.value = value
		self.max_d = max_depth
		self.visited = set()
		self.result = self.algorithm(graph)

	def algorithm(self, g):
		for vtx in g.V():
			if(vtx in self.visited): continue
			self.visited.add(vtx)
			res = self.__dfs_subroutine__(g, vtx, 0)
			if(res != None): return res
		return None

	def __dfs_subroutine__(self, g, v, depth):
		if(depth > self.max_d and self.max_d != -1): return None

		for neigh in g.neighbors(v):
			if(neigh in self.visited): continue
			self.visited.add(neigh)
			self.__dfs_subroutine__(g, neigh, depth+1)

		if(g.data[v][self.key] == self.value): 
			return v
		else:
			return None

############################
# ALGORITHM: Depth-First Traversal (DFT)
# ~ Takes a Graph and a start vertex as input. A depth
# ~ First Traversal is performed starting at the start 
# ~ vertex. If one is not specified, the entire graph is
# ~ traversed.
#
# IMPLEMENTATION:
# ~ A DFT recursively visits the children of each node
# ~ before visiting the node itself. In large unbounded 
# ~ graphs, it would be wise to limit the DFT with a 
# ~ maximum depth to make it a Limited Depth First Traversal.
# ~ This functionality is available here.
############################
class DFT:
	def __init__(self, graph, start=None, max_depth=-1):
		self.max_d = max_depth
		self.visited = set()
		self.post = []
		self.tree = Graph(graph.attrs)
		self.algorithm(graph, start)

	def algorithm(self, g, s):
		if(s == None):
			for v in g.V():
				if(v in self.visited): continue
				self.visited.add(v)
				self.__dfs_subroutine__(g, v, 0)
		else:
			self.visited.add(s)
			self.__dfs_subroutine__(g, s, 0)

	def __dfs_subroutine__(self, g, v, depth):
		if(depth > self.max_d and self.max_d != -1): return
		self.tree.add_vertex(v)

		for neigh in g.neighbors(v):
			self.tree.add_edge(g.adj[v][neigh])
			if(neigh in self.visited): continue
			self.visited.add(neigh)
			self.__dfs_subroutine__(g, neigh, depth+1)

		self.post.append(v)

	def postorder(self):
		return self.post

############################
# ALGORITHM: Spanning Tree
# ~ Takes a Graph as input, and returns a spanning tree
# ~ of the graph. A spanning tree is a minimal acyclic set of
# ~ connected edges such that every vertex in the graph
# ~ is an endpoint of at least one edge in the set.
# 
# IMPLEMENTATION:
# ~ Perform a Breadth-First Traversal. Along the way, if a
# ~ Non-tree edge is encountered, remove it from the graph.
############################
class SpanningTree:

	def __init__(self, graph):
		self.tree = graph.dup()
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
# ALGORITHM: Cycle Count
# ~ Takes a Graph as input, and returns the number of simple
# ~ cycles in the graph.
#
# IMPLEMENTATION:
# ~ Find a Spanning Tree of the graph. The number of edges
# ~ in the graph that aren't in the spanning tree (Non-tree
# ~ edges) is the number of cycles.
############################
class CycleCount:

	def __init__(self, graph):
		self.cycles = 0
		self.algorithm(graph)

	def algorithm(self, g):
		g_edges = len(g.E)
		st = SpanningTree(g)
		self.cycles = g_edges- len(st.tree.E)

	def is_acyclic(self):
		return self.cycles == 0

############################
# ALGORITHM: Kruskal's Minimum Spanning Tree
# ~ Takes a Graph as input, and returns an MST
# ~ of the graph. An MST is a maximal acyclic set of
# ~ connected edges with minimum total weight such that
# ~ every vertex in the graph is an endpoint of at 
# ~ least one edge in the set.
# 
# IMPLEMENTATION:
# ~ Create a new graph with no edges and the same vertices
# ~ as the old graph. Sort the edges of the old graph by weight.
# ~ Add edges into the new graph in increasing order of weight
# ~ as long as they don't create cycles. Cycle detection in this
# ~ case is done via a Union-Find to determine whether endpoints
# ~ have the same component membership.
############################
class KruskalMST:

	def __init__(self, graph):
		self.tree = Graph({"weighted" : True})
		self.min_weight = 0
		if(not graph.is_directed()):
			self.algorithm(graph)

	def edge_wt_sort(self, edge):
		return edge.wt

	def algorithm(self, graph):
		edges = sorted(graph.E, key=self.edge_wt_sort)

		uf = UnionFind()
		for vtx in graph.V():
			uf.makeset(vtx)

		for edge in edges:
			par_v1 = uf.find(edge.v1)
			par_v2 = uf.find(edge.v2)
			if(par_v1 == par_v2): continue

			self.tree.add_edge(edge)
			self.min_weight += edge.wt
			uf.union(edge.v1, edge.v2)

	def mst(self):
		return self.tree

	def weight(self):
		return self.min_weight

############################
# ALGORITHM: Prim's Minimum Spanning Tree
# ~ Takes a Graph as input, and returns an MST
# ~ of the graph. An MST is a maximal acyclic set of
# ~ connected edges with minimum total weight such that
# ~ every vertex in the graph is an endpoint of at 
# ~ least one edge in the set.
# 
# IMPLEMENTATION:
# ~ Create a new graph with no edges and the same vertices
# ~ as the old graph. Sort the edges of the old graph by weight.
# ~ Add the cheapest edge to the new graph, then insert all of its
# ~ adjoining edges onto a MinHeap. Continue this until inserting
# ~ another edge into the new graph would create a cycle.
############################
class PrimMST:

	def __init__(self, graph):
		self.tree = Graph({"weighted" : True})
		self.min_weight = 0
		if(not graph.is_directed()):
			self.algorithm(graph)

	def edge_wt_sort(self, edge):
		return edge.wt

	def algorithm(self, graph):
		edges = sorted(graph.E, key=self.edge_wt_sort)

		hp = MinHeap()
		hp.insert(edges[0])

		while(not hp.empty()):
			edge = hp.pop()
			graph.remove_edge(edge)
			if(edge.v1 in self.tree.V() \
				and edge.v2 in self.tree.V()): continue
			
			self.tree.add_edge(edge)
			self.min_weight += edge.wt
			neighborhood = graph.edges(edge.v1) + graph.edges(edge.v2)
			hp.insert_all(neighborhood)

	def mst(self):
		return self.tree

	def weight(self):
		return self.min_weight

############################
# ALGORITHM: Kosaraju's Strongly Connected Component Detection
# ~ Takes a Graph as input, and returns a list of SCC's of the graph 
# ~ (as directed Graphs). A SCC is a set of vertices such that
# ~ any vertex v in the set can be reached by any other vertex c
# ~ via a directed path from v to c.
# 
# IMPLEMENTATION:
# ~ Build a Breadth first search tree (BFST) from the original
# ~ graph. Then, reverse the graph and start the search in the
# ~ same order. Any nodes that are reached in both searches from
# ~ the same starting point are part of the same strongly 
# ~ connected component.
############################
class KosarajuSCC:

	def __init__(self, graph):
		self.sccs = []
		self.scc_map = {}
		if(graph.is_directed()):
			self.algorithm(graph)

	def algorithm(self, g):
		dft = DFT(g)
		gr = g.reverse()

		for v in reversed(dft.postorder()):
			if(v in self.scc_map): continue
			dftR = DFT(gr, v)
			post = dftR.postorder()
			rev = dftR.tree.reverse()
			for v in post:
				self.scc_map[v] = rev
				gr.remove_vertex(v)

			self.sccs.append(rev)

	def components(self):
		return self.sccs

	def strongly_connected(self):
		return len(self.sccs) == 1

	def num_components(self):
		return len(self.sccs)

	def strong_component_of(self, vertex):
		return self.scc_map[vertex]

		

############################
# ALGORITHM: Tarjan's Bridge Detection
# ~ Takes a Graph as input, and returns a list of Bridges of the graph 
# ~ (as Edges). A bridge is an edge such that its removal from the
# ~ graph would increment the number of components. This version is
# ~ based off of the implementation by Robert Sedgewick and Kevin Wayne.
# 
# IMPLEMENTATION:
# ~ The algorithm is based on the following principle: an edge is only
# ~ a bridge iff it is not part of any cycle. Therefore, performing simple
# ~ cycle detection (using a slightly different method than above) will
# ~ reveal all non-cycle edges. Cycle detection in this case is done with
# ~ a preorder traversal, and an auxiliary array named 'low'. Low[v] stores
# ~ the lowest preorder number on any path reachable through v. Therefore,
# ~ if low[v] is ever equal to pre[v], its preorder number, then the edge
# ~ (u,v) with pre[u] = pre[v] - 1 is a bridge.
############################
class Bridges:

	def __init__ (self, graph):
		self.edges = []
		self.pre = {}
		self.low = {}
		self.count = 1
		par = child = graph.random_vertex()
		self.algorithm(graph, par, child)

	def algorithm (self, g, par, child):
		self.pre[child] = self.count
		self.low[child] = self.pre[child]
		self.count+= 1

		for neigh in g.neighbors(child):

			if (neigh not in self.pre):
				self.algorithm(g, child, neigh)
				self.low[child] = min([self.low[child], self.low[neigh]])
				if (self.low[neigh] == self.pre[neigh]):
					self.edges.append(g.adj[child][neigh])

			elif (neigh != par): # takes care of parallel edges
				self.low[child] = min([self.low[child], self.pre[neigh]])

	def bridges(self):
		return self.edges

	def num_bridges(self):
		return len(self.edges)

############################
# ALGORITHM: Articulation Point Detection
# ~ This algorithm follows from bridge detection: the endpoints of
# ~ any bridge are articulation points as long as their degree is
# ~ greater than 1. Therefore, the problem of
# ~ finding all articulation points in a graph is reduced to finding 
# ~ all bridges in a graph.
# 
# IMPLEMENTATION:
# ~ Find all bridges using Tarjan's algorithm. Their endpoints
# ~ comprise the set of articulation points.
############################
class ArticulationPoints:

	def __init__(self, graph):
		self.points = set()
		self.algorithm(graph)

	def algorithm(self, g):
		b = Bridges(g)
		if(b.num_bridges() == 0):
			return

		for e in b.bridges():
			for v in e.endpoints():
				if(v in self.points): continue
				if(g.degree(v) <= 1): continue

				self.points.add(v)

	def articulation_points(self):
		return self.points

	def num_articulation_points(self):
		return len(self.points)