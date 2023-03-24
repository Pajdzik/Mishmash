#!/usr/bin/env ruby

# @param {Integer[]} nums
# @param {Integer} key
# @param {Integer} k
# @return {Integer[]}
def find_k_distant_indices(nums, key, k)
    result = []
    i = 0
    last_end_index = 0

    while i < nums.size do
        if nums[i] == key
            start_index = [last_end_index, i - k].max
            end_index = [i + k, nums.size - 1].min
            result.push(*(start_index..end_index).to_a)
            last_end_index = end_index + 1
        end
        i += 1
    end
    result
end

if __FILE__ == $0
    puts find_k_distant_indices([2,2,2,2,2], 2, 2)
end