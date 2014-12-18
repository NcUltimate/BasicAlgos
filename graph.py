import random
from common import Edge
from graph_algs import Bipartite
from other_algs import UnionFind

############################
# DATA STRUCTURE: GraphAttributes
# ~ Holds several values that describe
# ~ a graph. Useful for printing.
############################
class GraphAttributes:
	def __init__(self, attr_map={}):
		# graph properties 
		self.directed = attr_map['directed'] if 'directed' in attr_map  else False
		self.weighted = attr_map['weighted'] if 'weighted' in attr_map  else False
		self.capacious = attr_map['capacious'] if 'capacious' in attr_map else False

		# require algorithmic computation. used
		# for caching the results for successive queries.
		self.acyclic = attr_map['acyclic'] if 'acyclic' in attr_map else None
		self.bipartite = attr_map['bipartite'] if 'bipartite' in attr_map else None
		self.connected = attr_map['connected'] if 'connected' in attr_map else None
		self.regular = attr_map['regular'] if 'regular' in attr_map else None

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
# ~ Constructor initializes an empty graph, to which edges and vertices
# ~ can be added. Severl utility methods exist for obtaining such
# ~ information as degree, neighbors, bipartiteness, and more.
# ~ TODO: Implement initializer methods from common graph file types.
############################
class Graph:
	def __init__(self, attributes = GraphAttributes()):
		self.E = []
		self.data = {}
		self.adj = {}
		self.attrs = attributes

	def init_from_graph(self, g2):
		self.E = g2.E()
		self.data = g2.data
		self.adj = g2.adj
		self.attrs = g2.attrs

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
		if(id2 in self.adj[id1] or \
			 (not self.attrs.directed and id1 in self.adj[id2])): return
		
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
	def V(self): return self.adj.keys()
	def num_vertices(self): return len(self.V())
	def num_edges(self): return len(self.E())
	def is_directed(self): return self.attrs.directed
	def is_capacious(self): return self.attrs.capacious
	def is_weighted(self): return self.attrs.weighted
	def is_connected(self): 
		if(self.attrs.connected != None): return self.attrs.connected

		self.attrs.connected = ConnectedComponents(self).is_connected()
		return self.attrs.connected
		
	def is_bipartite(self): 
		if(self.attrs.bipartite != None): return self.attrs.bipartite

		self.attrs.bipartite = Bipartite(self).is_bipartite()
		return self.attrs.bipartite

	def is_acyclic(self): return False
	def is_regular(self): return False