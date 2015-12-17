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
        (1...ary.size).each do |j|
          (0...ary.size-j).each do |k|
            if ary[k] > ary[k+1]
              temp      = ary[k]
              ary[k]    = ary[k+1]
              ary[k+1]  = temp
            end
          end
        end
        ary
      end

      ############################
      # INSERTION SORT
      # An intuitive O(n^2) sort.
      def insertion_sort(ary)
        (1...ary.size).each do |j|
          k = j
          while k > 0 && ary[k] < ary[k-1]
            temp      = ary[k]
            ary[k]    = ary[k-1]
            ary[k-1]  = temp
            k         -= 1
          end
        end
        ary
      end

      ############################
      # SELECTION SORT
      # Find n minimums for an O(n^2) sort.
      def selection_sort(ary)
        ary.size.times do |j|
          min, m = ary[j], j
          (j...ary.size).each do |k|
            min, m = ary[k], k if ary[k] < min
          end
          temp      = ary[j]
          ary[j]    = ary[m]
          ary[m]    = temp
        end
        ary
      end

      ############################
      # MERGE SORT
      # A fast, stable O(nlogn) sort.
      def merge_sort(ary)
        return ary         if ary.size <= 1
        return ary.minmax  if ary.size == 2

        m1 = merge_sort(ary[0...ary.size/2])
        m2 = merge_sort(ary[ary.size/2..-1])

        ary2, k, j = [], 0, 0
        while !(j==m1.size && k==m2.size)
          if j == m1.size
            ary2 += m2[k..-1]
            break
          end
          if k == m2.size
            ary2 += m1[j..-1]
            break
          end

          if m1[j] < m2[k]
            ary2 << m1[j]
            j += 1
          elsif m1[j] > m2[k]
            ary2 << m2[k]
            k += 1
          elsif m1[j] == m2[k]
            ary2 << m1[j] << m2[k]
            j += 1
            k += 1
          end
        end
        ary2
      end

      ############################
      # QUICK SORT
      # A fast, in-place O(nlogn) sort. Up to O(n^2).
      def quick_sort(ary)
        return ary         if ary.size <= 1
        return ary.minmax  if ary.size == 2

        # pick a random pivot for now...
        piv = (Random.rand() * ary.size).to_i
        q1  = quick_sort(ary[0...piv])
        q2  = quick_sort(ary[piv..-1])

        # TODO: finish qsort
      end

      ############################
      # BUCKET SORT
      # An O(n) sort, yay.
      def bucket_sort(ary)
        # TODO: finish bucket sort
      end

      ############################
      # RADIX SORT
      # An O(n) sort, yay.
      def radix_sort(ary)
        # TODO: finish radix sort
      end

    end
  end
end

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
array = (1..10_000).to_a.shuffle
algos = %i[bubble_sort insertion_sort selection_sort merge_sort
          quick_sort ruby_sort]
Benchmark.bm do |x|
  algos.each do |algo|
    x.report("#{algo}".ljust(20)){ Algorithms::Sorting.send(algo, array.dup) }
  end
end
