import common as com
import graph as g
import graph_algs as ga

def basic_test():
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

def weighted_test():
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
	
	print("Minimum Spanning Tree:")
	mst = ga.KruskalMST(g1)
	print(mst.mst().E)
	print(mst.weight())

def main():
	basic_test()
	weighted_test()

main()