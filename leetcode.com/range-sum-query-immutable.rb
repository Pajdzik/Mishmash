class NumArray
    def initialize(nums)
        @nums = nums

        s = 0
        @sums = []

        nums.each_with_index do | el, i |
            @sums[i] = s
            s += el
        end
    end

    def foo
        puts @sums
        puts @nums
    end
    
    def sum_range(left, right)
        @sums[right] - @sums[left] + @nums[right]
    end
end
