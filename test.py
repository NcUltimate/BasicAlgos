import common as com
import graph as g
import graph_algs as ga
import heap as h

# basic graph functionality test
def graph_test_1():
	graph1 = g.Graph()
	graph1.connect(1,2)
	graph1.connect(2,3)
	graph1.connect(3,4)
	graph1.connect(4,5)
	graph1.connect(5,1)
	graph1.connect(5,2)
	graph1.connect(4,2)
	graph1.connect(6,7)
	graph1.connect(7,8)
	graph1.connect(6,8)
	
	cc = ga.ConnectedComponents(graph1)
	bp = ga.Bipartite(graph1)
	cd = ga.CycleCount(graph1)

	print("Connected Components: "+str(cc.components()))
	print("It is "+("not" if not bp.is_bipartite() else "") + " bipartite.")
	print("It "+("is acyclic" if cd.cycles == 0 else "has "+str(cd.cycles)+" cycles."))

# MST test
def graph_test_2():
	g1 = g.Graph({'weighted' : True})
	g1.connect(1,2,2)
	g1.connect(2,3,4)
	g1.connect(3,4,8)
	g1.connect(4,5,6)
	g1.connect(5,6,2)
	g1.connect(5,2,7)
	g1.connect(6,2,3)
	g1.connect(6,7,5)
	g1.connect(7,8,4)
	g1.connect(8,1,5)
	
	print("Kruskal's MST Algorithm:")
	mst = ga.KruskalMST(g1)
	print(mst.mst().E)
	print(mst.weight())

	print("Prim's MST Algorithm:")
	mst = ga.PrimMST(g1)
	print(mst.mst().E)
	print(mst.weight())

def heap_test():
	heap = h.Heap()
	heap.insert(100)
	heap.insert(25)
	heap.insert(17)
	heap.insert(2)
	heap.insert(19)
	heap.insert(3)
	heap.insert(36)
	heap.insert(7)
	heap.insert(1)
	minheap = h.MinHeap()
	maxheap = h.MaxHeap()
	minheap.merge(heap)
	maxheap.merge(heap)


	print("------ heap ------")
	print("Heap Size: "+str(heap.size()))
	heap.pretty_print()
	# should print in increasing order
	while(not heap.empty()):
		print(heap.pop())

	print("------ minheap ------")
	print("MinHeap Size: "+str(minheap.size()))
	minheap.pretty_print()
	# should print in increasing order
	while(not minheap.empty()):
		print(minheap.pop())

	print("------ maxheap ------")
	print("MaxHeap Size: "+str(maxheap.size()))
	maxheap.pretty_print()
	# should print in decreasing order
	while(not maxheap.empty()):
		print(maxheap.pop())

def main():
	heap_test()
	graph_test_1()
	graph_test_2()


main()