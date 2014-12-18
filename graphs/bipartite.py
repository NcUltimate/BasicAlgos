############################
# ALGORITHM: Bipartite
# ~ Takes a Graph as input. If the graph is bipartite, the
# ~ algorithm will successfully split it into two accessible
# ~ bipartitions. If not, the bipartitions will remain
# ~ empty, and is_bipartite will return False.
#
# IMPLEMENTATION
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