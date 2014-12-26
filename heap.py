############################
# DATA STRUCTURE: Heap
# ~ Constructor initializes an empty heap, to which nodes
# ~ can be inserted or deleted. Heaps can be set to be min 
# ~ or max at the time of initialization.
############################
class Heap:

	def __init__(self, min=True):
		self.root = None
		self.min = min

	def __insert__(self, value, subtree):
		pass

	def insert(self, value):
		self.__insert__(self, value, self.root)
