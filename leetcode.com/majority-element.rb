# @param {Integer[]} nums
# @return {Integer}
def majority_element_bf(nums)
    counter = Hash.new(0)
    nums.each { |num| counter[num] += 1 }
    k, v = counter.max_by {|k, v| v}
    k
end

def majority_element(nums)
    major = nil
    count = 0

    nums.each do |num|
        major = num if count == 0
        count += (num == major ? 1 : -1)
    end

    return major
end