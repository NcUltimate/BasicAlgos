module Basic
  class PriorityQueue < SimpleDelegator
    attr_accessor :compare

    def initialize(compare = default_compare)
      super([])
      self.compare = compare
    end

    def <<(el)
      insert(bindex(el), el)
    end

    def +(array)
      pq = PriorityQueue.new(compare)
      pq.__setobj__(__getobj__)
      array.each(&pq.method(:<<))
      pq
    end

    def bindex(el, s = 0, e = length-1)
      m = (s + e)/2
      return s if s > e

      cmp = compare.call(el, self[m])
      if cmp == 1
        return bindex(el, m + 1, e)
      elsif cmp == -1
        return bindex(el, s, m - 1)
      else
        return m
      end
    end

    private

    def default_compare
      lambda{ |a, b| a <=> b }
    end
  end
end