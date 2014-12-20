import common as com
import graph as g
import graph_algs as ga

def main():
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
	cd = ga.CycleDetection(graph1)
	print(graph1.E)
	print(graph1.attrs.modifier_list())
	print(cc.components())
	print(bp.is_bipartite())
	print(cd.cycles)

main()