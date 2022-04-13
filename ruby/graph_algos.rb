module Basic
  module Algorithms
    class Graph
      class << self
        def mst(graph)
          if graph.is_a?(WeightedGraph)
            _weighted_mst(graph)
          else
            _mst(graph)
          end
        end

        private

        def _weighted_mst(graph)
          result = Basic::WeightedGraph.new
          return result unless graph.edges.any?

          sorted = []
          spanned = {}
          graph.edges.each do |n1, weights|
            weights.each do |n2, weight|
              sorted << [n1, n2, weight]
            end
          end

          sorted = sorted.sort_by { |s| s[2] }

          sorted.each do |(n1, n2, wt)|
            next if spanned[n1] && spanned[n2]
            result.add_edge(n1, n2, wt)
            spanned[n1] = true
            spanned[n2] = true
            break if result.size == graph.size
          end

          result
        end

        def _mst(graph)
          result = Basic::Graph.new
          return result unless graph.edges.any?

          spanned = {}
          graph.edges.each do |n1, nodes|
            nodes.each do |n2|
              next if spanned[n1] && spanned[n2]
              spanned[n2] = true
              result.add_edge(n1, n2)
            end
            spanned[n1] = true
            break if result.size == graph.size
          end
          result
        end
      end
    end
  end
end