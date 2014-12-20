import common as com
import graph as g
import graph_algs as ga

def main():
	graph1 = g.Graph()
	graph1.add_vertex(1)
	graph1.add_vertex(2)
	graph1.add_vertex(3)
	graph1.add_vertex(4)
	graph1.add_vertex(5)
	graph1.connect(1,2)
	graph1.connect(2,3)
	graph1.connect(3,4)
	graph1.connect(4,5)
	graph1.connect(5,1)
	graph1.connect(5,2)
	graph1.connect(4,2)

	bp = ga.Bipartite(graph1)
	cd = ga.CycleDetection(graph1)
	print(bp.is_bipartite())
	print(cd.cycles)

main()