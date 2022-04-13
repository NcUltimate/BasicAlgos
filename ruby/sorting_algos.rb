class Algorithms
  class Sorting
    class << self

      ############################
      # RUBY SORT
      # The system O(nlogn) sort.
      def ruby_sort(ary)
        ary.sort
      end

      ############################
      # BUBBLE SORT
      # Your textbook O(n^2) sort.
      def bubble_sort(ary)
        return ary if sorted?(ary)

        (1...ary.size).each do |j|
          (0...ary.size-j).each do |k|
            next if (ary[k] <=> ary[k+1]) < 1
            
            swap(ary, k, k+1)
          end
        end
        ary
      end

      ############################
      # INSERTION SORT
      # An intuitive O(n^2) sort.
      def insertion_sort(ary)
        return ary if sorted?(ary)

        (1...ary.size).each do |j|
          j.downto(1) do |k|
            break if (ary[k] <=> ary[k-1]) > -1

            swap(ary, k, k-1)
          end
        end
        ary
      end

      ############################
      # SELECTION SORT
      # Find n minimums for an O(n^2) sort.
      def selection_sort(ary)
        return ary if sorted?(ary)

        ary.size.times do |j|
          min, m = ary[j], j
          (j...ary.size).each do |k|
            if (ary[k] <=> min) == -1
              min, m = ary[k], k
            end
          end

          swap(ary, j, m)
        end
        ary
      end

      ############################
      # MERGE SORT
      # A fast, stable O(nlogn) sort.
      def merge_sort(ary, s=0, e=ary.size-1)
        return [ary[s]] if e <= s

        m = (s+e)/2 + 1
        m1 = merge_sort(ary, s, m-1)
        m2 = merge_sort(ary, m, e)
        
        merge(m1, m2)
      end


      ############################
      # HEAP SORT
      # A fast O(nlogn) sort.
      def heap_sort(ary)
        # TODO: implement heapsort
        ary.sort
      end

      ############################
      # QUICK SORT
      # A fast, in-place O(nlogn) sort.
      # Redundant shuffle kills possibility of O(n^2).
      def quick_sort(ary, s=0, e=ary.size-1, d=0)
        return ary[s] if e == s

        piv = s
        s.upto(e) do |idx|
          if (ary[idx] <=> ary[e]) == -1
            swap(ary, piv, idx) unless idx == piv
            piv += 1
          end
        end
        swap(ary, piv, e)

        quick_sort(ary, s, piv - 1, 1)  if piv > s
        quick_sort(ary, piv + 1, e, 1)  if piv < e
        ary
      end

      ############################
      # BUCKET SORT
      # An O(nlog(n/k)) sort, yay.
      def bucket_sort(ary, sort_algo = :merge_sort, num_buckets = 20)
        bucket_size = [ary.size / num_buckets, 5].max

        # I use merge_sort by default for sorting the buckets.
        buckets = ary.each_slice(bucket_size).map { |bucket| send(sort_algo, bucket) }

        # TODO: We need a Priority Queue for the k-way merge step.
        # I'm brute forcing it with a system sort & flatten for now.
        indices = (0..buckets.size-1).to_a
        indices.sort { |a,b| buckets[a][0] <=> buckets[b][0]}
        indices.map  { |idx| buckets[idx] }.flatten
      end

      def swap(ary, a, b)
        ary[a], ary[b] = ary[b], ary[a]
      end

      def merge(m1, m2)
        merged, k, j = [], 0, 0
        until j == m1.size || k == m2.size
          if (m1[j] <=> m2[k]) < 1
            merged << m1[j]
            j += 1
          end
          if (m2[k] <=> m1[j]) == -1
            merged << m2[k]
            k += 1
          end
        end
        merged << m1[j] and j += 1 until j == m1.size
        merged << m2[k] and k += 1 until k == m2.size
        merged
      end

      def sorted?(ary)
        asc = 0.upto(ary.size - 2).all? do |k|
          (ary[k] <=> ary[k + 1]) < 1
        end
        return true if asc

        0.upto(ary.size - 2).all? do |k|
          (ary[k] <=> ary[k + 1]) > -1
        end
      end
    end
  end
end

def main
  array = (1..100).to_a.sample(20).shuffle
  puts "#{array}"
  puts "----------------------"
  algos = %i[ruby_sort quick_sort bubble_sort   
              selection_sort insertion_sort merge_sort]
  algos.each do |algo|
    res = Algorithms::Sorting.send(algo, array.dup)
    puts "#{res} --> #{algo}"
  end

  puts
  puts "Benchmarking..."
  puts
  require 'benchmark'
  array = (1..50_000_000).to_a
  Benchmark.bm do |x|
    algos.each do |algo|
      x.report("#{algo}".ljust(20)) do
        Algorithms::Sorting.send(algo, array.dup)
      end
    end
  end
end
#main
