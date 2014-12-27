import random
from common import Edge

############################
# DATA STRUCTURE: Graph
# ~ Constructor initializes an empty graph, to which edges and vertices
# ~ can be added. Severl utility methods exist for obtaining such
# ~ information as degree, neighbors, bipartiteness, and more.
# ~ TODO: Implement initializer methods from common graph file types.
#
# RECOGNIZED ATTRIBUTES:
# ~ 'weighted' : graph has weighted edges
# ~ 'directed' : graph has directed edges
# ~ 'capacious' : graph edges have capacity
############################
class Graph:
	def __init__(self, attrs={}):
		self.E = []
		self.data = {}
		self.adj = {}

		defaults = {'weighted':False,
					'directed':False,
					'capacious':False }
		self.attrs = dict(defaults.items() + attrs.items())

	def init_from_graph(self, g2):
		self.data = dict(g2.data)
		self.attrs = dict(self.attrs.items() + g2.attrs.items())
		for v in g2.V():
			self.add_vertex(v)
		for e in g2.E:
			self.add_edge(e)

	def dup(self):
		new_graph = Graph()
		new_graph.init_from_graph(self)
		return new_graph

	# graph modifier methods
	def add_vertices(self, vtxs):
		for v in vtxs: self.add_vertex(v)

	def add_vertex(self, v, data = {}):
		if(v in self.V()): return

		self.data[v] = data
		if('id' not in self.data[v]): self.data[v]['id'] = v
		if('name' not in self.data[v]): self.data[v]['name'] = v

		self.adj[v] = {}

	def add_edges(self, edges):
		for edge in edges: 
			self.add_edge(edge)

	def add_edge(self, edge):
		# add endpoints if thet aren't already
		# in the graph
		self.add_vertices(edge.endpoints())

		# duplicate detection
		if(edge.v2 in self.adj[edge.v1] or \
			 (not self.attrs['directed'] \
			 	and edge.v1 in self.adj[edge.v2])): return

		if(self.attrs['directed']):
			self.adj[edge.start()][edge.end()] = edge
		else:
			self.adj[edge.v1][edge.v2] = edge
			self.adj[edge.v2][edge.v1] = edge

		self.E.append(edge)

	def connect(self, id1, id2, wt=None, cap=None):
		edge = Edge(id1, id2, self.attrs['directed'], wt, cap)
		self.add_edge(edge)

	def disconnect(self, v1, v2):
		if(v1 not in self.adj): return
		if(v2 not in self.adj[v1]): return

		self.E.remove(self.adj[v1][v2])
		del self.adj[v1][v2]

		if(not self.attrs['directed']):
			del self.adj[v2][v1]

	def remove_edge(self, edge):
		if(edge not in self.E): return
		self.disconnect(edge.v1, edge.v2)

	def remove_vertex(self, vtx):
		if(vtx not in self.adj): return
		for n in self.adj:
			if(vtx in self.adj[n]): 
				self.E.remove(self.adj[n][vtx])
				del self.adj[n][vtx]

		if(vtx in self.adj):
			keys = self.adj[vtx].keys()
			for n in keys:
				self.E.remove(self.adj[vtx][n])
				del self.adj[vtx][n]
			del self.adj[vtx]

	# utility methods
	def connected(self, v1, v2): 
		return (v2 in self.adj[v1]) \
				or(v1 in self.adj[v2])

	def neighbors(self, v): 
		return self.adj[v].keys()

	def edges(self, v):
		return [self.adj[v][v2] for v2 in self.adj[v]]

	def edges_from(self, v): 
		return self.edges(v)

	def edges_into(self, v):
		if(not self.attrs['directed']): 
			return self.edges(v)

		edges = [self.adj[vtx][v] for vtx in self.V() if v in self.adj[vtx]]
		return edges

	def degree(self, v): 
		return len(self.neighbors(v))

	def out_degree(self, v): 
		return self.degree(v)

	def in_degree(self, v): 
		return len(self.edges_into(v))

	def random_vertex(self): 
		return random.choice(self.V())

	def random_edge(self): 
		return random.choice(self.E())

	def cut(self, vertices):
		for v in vertices:
			self.remove_vertex(v)

	def compliment(self):
		g = Graph()
		for v1 in self.V():
			for v2 in self.V():
				if(v1 == v2): continue
				g.add_vertices([v1, v2])
				if(v1 not in self.adj or \
					v2 not in self.adj[v1]):
					g.connect(v1, v2)
		return g

	def reverse(self):
		g = Graph({'directed' : True})
		for v1 in self.V():
			g.add_vertex(v1)
			for v2 in self.adj[v1]:
				g.connect(v2, v1)
		return g

	def subgraph(self, vertices):
		g = Graph()
		for v1 in vertices:
			if(v1 not in self.adj): continue
			g.add_vertex(v1)
			for v2 in self.adj[v1]:
				g.add_edge(self.adj[v1][v2])
		return g

	def equals(self, g2):
		if(isinstance(g2, self.__class__)):
			numV1, numV2 = len(self.V()), len(g2.V())
			numE1, numE2 = len(self.E), len(g2.E)
			if(numV1 != numV2 or numE1 != numE2): return False

			for v1 in self.adj:
				for v2 in self.adj[v1]:
					if(v1 not in g2.adj): return False
					if(v2 not in g2.adj[v1]): return False
					if(not self.adj[v1][v2].equals(g2.adj[v1][v2])): return False

			return True
		else:
			return False

	def __eq__(self, other):
		return self.equals(other)

	def __str__(self):
		return str(self.E) if self.E else str(self.V())

	def __repr__(self):
		return self.__str__()

	# attribute modifiers
	def set_directed(self, directed): 
		self.attrs['directed'] = directed

	def set_flowgraph(self, capacious): 
		self.attrs['capacious'] = capacious

	def set_weighted(self, weighted): 
		self.attrs['weighted'] = weighted

	# accessor methods
	def V(self): 
		return self.adj.keys()

	def num_vertices(self): 
		return len(self.V())

	def num_edges(self): 
		return len(self.E)

	def is_directed(self): 
		return self.attrs['directed']

	def is_flowgraph(self): 
		return self.attrs['capacious']

	def is_weighted(self): 
		return self.attrs['weighted']