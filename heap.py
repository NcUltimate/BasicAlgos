from common import Node

############################
# DATA STRUCTURE: Heap
# ~ Constructor initializes an empty heap, to which nodes
# ~ can be inserted or deleted. Heaps can be set to be min 
# ~ or max at the time of initialization. THis data structure
# ~ Is commonly used for MinHeaps, MaxHeaps, and Priority Queues.
#
#~ NOTE: This data strucute uses the __cmp__ method to allow the
# ~ comparison of any object. To 'heapify' any object or type,
# ~ simply override this method to define your own comparison with
# ~ another object of the same type.
#
# RUNNING TIME:
# ~ Insert: O(lg(n))
# ~ Pop: O(lg(n))
# ~ Merge: O(mlg(n+m))
# ~ Peek: O(1)
############################
class Heap:

	def __init__(self, minheap=True):
		self.root = None
		self.heap_type = -1 if minheap else 1

		# dictionary to keep track of subtree sizes.
		# this keeps the tree balanced when inserting.
		self.cts = {}

	def __swap__(self, node1, node2):
		temp = node1.value
		node1.value = node2.value
		node2.value = temp

	def __sink__(self, node, left_child=True):
		if(node.is_leaf()):
			temp = node.value
			if(not node.is_root()):
				if(left_child):
					node.parent.left(None)
				else:
					node.parent.right(None)
			else:
				self.root = None
			del self.cts[node]
			del node
			return temp
		else:
			self.cts[node] -= 1
			if(node.rchild == None):
				self.__swap__(node, node.lchild)
				return self.__sink__(node.lchild)
			elif(node.lchild == None):
				self.__swap__(node, node.rchild)
				return self.__sink__(node.rchild, False)
			else:
				if(node.lchild.value.__cmp__(node.rchild.value) == self.heap_type):
					self.__swap__(node, node.lchild)
					return self.__sink__(node.lchild)
				else:
					self.__swap__(node, node.rchild)
					return self.__sink__(node.rchild, False)

	def __bubble__(self, node):
		if(node.parent == None): return
		if(node.value.__cmp__(node.parent.value) == self.heap_type):
			self.__swap__(node, node.parent)
			self.__bubble__(node.parent)

	def __findleaf__(self, value, node):
		self.cts[node] += 1
		if(node.lchild and node.rchild):
			if(self.cts[node.lchild]< self.cts[node.rchild]):
				self.__findleaf__(value, node.lchild)
			else:
				self.__findleaf__(value, node.rchild)
		else:
			newnode = Node(value)
			self.cts[newnode] = 1
			if(not node.lchild):
				node.left(newnode)
			else:
				node.right(newnode)
			newnode.parent = node
			self.__bubble__(newnode)

	def insert_all(self, values):
		for value in values:
			self.insert(value)
	def insert(self, value):
		if(self.root == None):
			self.root = Node(value)
			self.cts[self.root] = 1
		else:
			self.__findleaf__(value, self.root)

	def peek(self):
		if(self.empty()): return
		return self.root.value

	def pop(self):
		if(self.empty()): return
		return self.__sink__(self.root)

	def empty(self):
		return self.root == None

	def __mergeheap__(self, root):
		self.insert(root.value)
		if(root.lchild != None):
			self.__mergeheap__(root.lchild)
		if(root.rchild != None):
			self.__mergeheap__(root.rchild)

	def merge(self, heap2):
		if(heap2.empty()): return
		self.__mergeheap__(heap2.root)

	def __pp__(self, node, depth=0):
		if(node == None): return

		print(" "*depth + str(node.value)+" ("+str(self.cts[node])+")")
		self.__pp__(node.lchild, depth+1)
		self.__pp__(node.rchild, depth+1)

	def size(self):
		return self.cts[self.root]

	def pretty_print(self):
		self.__pp__(self.root, 0)

############################
# DATA STRUCTURE: PriorityQueue
# ~ A wrapper for a heap.
#
# ~ NOTE: Priority is based on equality operators. If objects are being
# ~ inserted into the priority queue, make sure to define the __cmp__()
# ~ method so that <, <=, > >=, and == methods are defined for the object.
############################
class PriorityQueue(Heap):

	def enqueue(self, value):
		self.insert(value)

	def dequeue(self):
		return self.pop()

############################
# DATA STRUCTURE: MinHeap
# ~ A wrapper for a heap. Initializes a minimum heap.
############################
class MinHeap(Heap):

	def __init__(self):
		Heap.__init__(self, True)


############################
# DATA STRUCTURE: MinHeap
# ~ A wrapper for a heap. Initializes a minimum heap.
############################
class MaxHeap(Heap):

	def __init__(self):
		Heap.__init__(self, False)
