require 'set'
require 'json'

module Basic
  class Graph
    attr_accessor :nodes, :edges

    def initialize(edges = {}, nodes = [])
      self.edges = edges
      self.nodes = Set.new(nodes)
      add_nodes(edges.keys)
      add_nodes(edges.values.flatten)
    end

    def add_node(node)
      self.nodes << node
    end

    def add_nodes(nodes)
      nodes.each do |node|
        self.nodes.add(node)
      end
    end

    def add_edge(n1, n2)
      self.edges[n1] ||= []
      self.edges[n1] << n2
      self.nodes << n1
      self.nodes << n2
    end

    def merge(graph)
      new_nodes = nodes + graph.nodes
      new_edges = edges.merge(graph.edges)
      self.class.new(new_edges, new_nodes)
    end

    def node?(node)
      nodes.member?(node)
    end

    def edge?(n1, n2)
      self.edges[n1].member?(n2) ||
        self.edges[n2].member?(n1)
    end

    def weighted?
      false
    end

    def size
      nodes.length
    end

    def random_node
      nodes.to_a.sample
    end

    def to_s
      JSON.pretty_generate(edges)
    end
  end
end