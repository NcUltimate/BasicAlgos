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
            next if ary[k] <= ary[k+1]
            
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
            break if ary[k] >= ary[k-1]

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
            min, m = ary[k], k if ary[k] < min
          end
          swap(ary, j, m)
        end
        ary
      end

      ############################
      # MERGE SORT
      # A fast, stable O(nlogn) sort.
      def merge_sort(ary, d = 0)
        return ary         if d == 0 and sorted?(ary)

        return ary         if ary.size <= 1
        return ary.minmax  if ary.size == 2

        m1 = merge_sort(ary[0...ary.size/2], d + 1)
        m2 = merge_sort(ary[ary.size/2..-1], d + 1)

        merge(m1, m2)
      end

      ############################
      # QUICK SORT
      # A fast, in-place O(nlogn) sort.
      # Redundant shuffle kills possibility of O(n^2).
      def quick_sort(ary, s=0, e=ary.size-1, d=0)
        return ary    if d == 0 and sorted?(ary)

        ary.shuffle!  if d == 0
        return ary[s] if e == s

        piv = s
        s.upto(e) do |idx|
          if ary[idx] < ary[e]
            swap(ary, piv, idx) unless idx == piv
            piv += 1
          end
        end
        swap(ary, piv, e)

        quick_sort(ary, s, piv - 1, d + 1)  if piv > s
        quick_sort(ary, piv + 1, e, d + 1)  if piv < e
        ary
      end

      ############################
      # BUCKET SORT
      # An O(nlog(n/k)) sort, yay.
      def bucket_sort(ary, sort_algo = :merge_sort, num_buckets = 20)
        bucket_size = [ary.size / num_buckets, 5].min

        # I use merge_sort by default for sorting the buckets.
        buckets = ary.each_slice(bucket_size).map { |bucket| send(sort_algo, bucket) }
        
        # TODO: We need a Priority Queue for the k-way merge step.
        # I'm brute forcing it with a system sort & flatten for now.
        indices = (0..buckets.size-1).to_a
        indices.sort { |a,b| buckets[a][0] <=> buckets[b][0]}
        indices.map  { |idx| buckets[idx] }.flatten
      end

      ############################
      # RADIX SORT
      # An O(n) sort, yay.
      def radix_sort(ary)
        # TODO: finish radix sort
      end

      def swap(ary, a, b)
        ary[a], ary[b] = ary[b], ary[a]
      end

      def merge(m1, m2)
        merged = []

        until m1.empty? || m2.empty?
          merged << m1.shift if m1[0] <= m2[0]
          merged << m2.shift if m2[0] > m1[0]
        end

        merged += m1 if m2.empty?
        merged += m2 if m1.empty?
        merged
      end

      def sorted?(ary)
        asc = 0.upto(ary.size - 2).all? do |k|
          ary[k] <= ary[k + 1]
        end
        return true if asc

        0.upto(ary.size - 2).all? do |k|
          ary[k] >= ary[k + 1]
        end
      end
    end
  end
end

def main
  array = (1..100).to_a.sample(20).shuffle
  puts "#{array}"
  puts "----------------------"
  algos = %i[bubble_sort insertion_sort selection_sort merge_sort
             quick_sort ruby_sort]
  algos.each do |algo|
    res = Algorithms::Sorting.send(algo, array.dup)
    puts "#{res} --> #{algo}"
  end

  puts
  puts "Benchmarking..."
  puts
  require 'benchmark'
  array = (1..1_000_000).to_a
  algos = %i[bubble_sort insertion_sort selection_sort merge_sort
            quick_sort ruby_sort]
  Benchmark.bm do |x|
    algos.each do |algo|
      x.report("#{algo}".ljust(20)) do
        Algorithms::Sorting.bucket_sort(array.dup, algo, 2000)
      end
    end
  end
end
#main
