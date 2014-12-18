import random
from common import Edge
from bipartite import Bipartite
from other/union_find import UnionFind

############################
# DATA STRUCTURE: GraphAttributes
# ~ Holds several values that describe
# ~ a graph. Useful for printing.
############################
class GraphAttributes:
	def __init__(self, attr_map):
		# graph properties 
		self.directed = 'directed' in attr_map ? attr_map['directed'] : False
		self.attrs.directed = 'weighted' in attr_map ? attr_map['weighted'] : False
		self.capacious = 'capacious' in attr_map ? attr_map['capacious'] : False

		# require algorithmic computation. used
		# for caching the results for successive queries.
		self.acyclic = 'acyclic' in attr_map ? attr_map['acyclic'] : None
		self.bipartite = 'bipartite' in attr_map ? attr_map['bipartite'] : None
		self.regular = 'regular' in attr_map ? attr_map['regular'] : None

	def modifier_list(self):
		modifiers = []
		modifiers.append('directed' if self.directed else 'undirected')
		modifiers.append('weighted' if self.weighted else 'unweighted')
		modifiers.append('acyclic'  if self.acyclic  else 'cyclic')
		if(self.bipartite): modifiers.append('bipartite')
		if(self.regular):   modifiers.append('regular')
		return modifiers


############################
# DATA STRUCTURE: Graph
# ~ Constructor initializes an empty
# ~ graph, to which edges and vertices
# ~ can be added. A couple utility methods
# ~ exist for initializing from certain file
# ~ types.
############################
class Graph:
	def __init__(self, attributes = GraphAttributes()):
		self.E = []
		self.data = {}
		self.adj = {}
		self.attrs = attributes
		# TODO: implement components 
		# via a union-find

	# graph modifier methods
	def add_vertices(self, vtxs):
		for v in vtxs: self.add_vertex(v)

	def add_vertex(self, v, data = {}):
		if(v in self.data): return

		self.data[v] = data
		if('id' not in self.data[v]): self.data[v]['id'] = v
		if('name' not in self.data[v]): self.data[v]['name'] = v

		self.adj[v] = {}

	def add_edges(self, edges):
		for edge in edges: self.add_edge(edge)

	def add_edge(self, edge):
		self.add_vertices(edge.endpoints())
		if(self.attrs.directed):
			self.adj[edge.start()][edge.end()] = edge
		else:
			self.adj[edge.v1][edge.v2] = edge
			self.adj[edge.v2][edge.v1] = edge

		self.E.append(edge)

	def connect(self, id1, id2):
		if(self.adj[id1][id2] or \
			 (not self.attrs.directed and self.adj[id2][id1])): return
		
		edge = Edge(id1, id2, self.attrs.directed)
		self.add_edge(edge)

	def disconnect(self, v1, v2):
		if(v2 in self.adj[v1]): 
			self.E.remove(self.adj[v1][v2])
			del self.adj[v1][v2]
		if(self.attrs.directed): return

		if(v1 in self.adj[v2]): 
			self.E.remove(self.adj[v2][v1])
			del self.adj[v2][v1]

	def remove_edge(self, edge):
		if(edge not in self.E()): return
		self.disconnect(edge.v1, edge.v2)

	def remove_vertex(self, vtx):
		for n in self.adj:
			if(vtx in self.adj[n]): 
				self.E.remove(self.adj[n][vtx])
				del self.adj[n][vtx]

		if(vtx in self.adj):
			for n in self.adj[vtx]:
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
		if(not self.attrs.directed): 
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

	# attribute modifiers
	def set_directed(self, directed): 
		self.attrs.directed = directed

	def set_capacious(self, capacious): 
		self.attrs.capacious = capacious
		
	def set_weighted(self, weighted): 
		self.attrs.weighted = weighted

	# accessor methods
	def V(): return self.adj.keys()
	def E(): return self.E
	def num_vertices(self): return len(self.V())
	def num_edges(self): return len(self.E())
	def is_directed(self): return self.attrs.directed
	def is_capacious(self): return self.attrs.capacious
	def is_weighted(self): return self.attrs.weighted
	def is_bipartite(self): 
		if(self.attrs.bipartite != None): return self.attrs.bipartite

		self.attrs.bipartite = Bipartite(self).is_bipartite()
		return self.attrs.bipartite

	def is_acyclic(self): return False
	def is_regular(self): return False