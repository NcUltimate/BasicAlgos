module Basic
  class Edge
    attr_accessor :from, :to, :weight, :directed

    def initialize(from, to, ops = {})
      self.from = from
      self.to = to
      self.weight = ops[:weight]
      self.directed = ops[:directed]
    end

    def weighted?
      self.weight
    end

    def directed?
      self.directed
    end
  end
end