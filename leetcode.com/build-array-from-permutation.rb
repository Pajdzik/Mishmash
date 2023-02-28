#!/usr/bin/env ruby

# @param {Integer[]} nums
# @return {Integer[]}
def build_array(nums)
    result = Array.new(nums.length)

    nums.each_with_index do | el, i |
        result[i] = nums[el]
    end

    result
end

puts build_array([0,2,1,5,3,4])