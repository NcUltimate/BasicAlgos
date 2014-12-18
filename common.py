
############################
# DATA STRUCTURE: Edge
# ~ General edge class with numerous attributes capable of fitting almost any algorithm.
# ~ If smaller edges are desired, such as an undirected unweighted edge, a set() can simply
# ~ be used.
############################
class Edge:

	def __init__(self, v1, v2, directed=False):
		self.v1 = v1
		self.v2 = v2
		self.dir = directed
		self.wt = None
		self.cap = None

	# modifier methods
	def set_weight(self, wt): self.wt = wt
	def set_capacity(self, cap): self.cap = cap
	def set_directed(self, directed): self.dir = directed

	# edge property accessors
	def weighted(self): return self.wt != None
	def capacious(self): return self.cap != None
	def directed(self): return self.dir

	# endpoint accessors
	def endpoints(self): return [self.v1, self.v2]
	def start(self): return self.v1 if self.dir else None
	def end(self): return self.v2 if self.dir else None

	# utility methods
	def contains(self, pt):
		return self.v1 == pt or self.v2 == pt

	def other(self, pt):
		return self.v1 if self.v2 == pt else self.v2

	def equals(self, e):
		if(isinstance(e, self.__class__)):
			if(e.wt == self.wt):
				if(not self.dir):
					return set(e.endpoints()) == set(self.endpoints()) 
				else:
					return e.v1 == self.v1 and e.v2 == self.v2
		else:
			return False

	def __eq__(self, other):
		return self.equals(other)

	def __str__(self):
		ret = str(self.v1)+"-"+(self.wt if self.weighted() else "")
		ret += ("/" + str(self.cap)) if self.capacious() else ""
		ret += "-"+str(self.v2)
		return ret

	def __repr__(self):
		return self.__str__();