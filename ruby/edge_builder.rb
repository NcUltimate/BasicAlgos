module Basic
  class EdgeBuilder
    class << self
      def from_hash(edge_hash, ops = {})
        if ops[:weighted]
          edge_hash.inject([]) do |(n1, weights), arr|
            weights.each do |n2, weight|
              edge_ops = ops.merge(weight: weight)
              arr << Edge.new(n1, n2, edge_ops)
            end
          end
        else
          edge_hash.inject([]) do |(n1, nodes), arr|
            nodes.each do |n2|
              arr << Edge.new(n1, n2, ops)
            end
          end
        end
      end

      def from_file(edge_file)

      end

      def from_array(edge_array)

      end
    end
  end
end