module Basic
  class WeightedGraph < Graph
    attr_accessor :weights

    def initialize(edges = {}, nodes = [])
      self.edges = edges
      self.nodes = Set.new(nodes)
      add_nodes(edges.keys)
      edges.values.each do |weights|
        add_nodes(weights.keys)
      end
    end

    def add_edge(n1, n2, weight = 0)
      self.edges[n1] ||= {}
      self.edges[n1][n2] = weight
      self.nodes << n1
      self.nodes << n2
    end

    def weighted?
      true
    end
  end
end