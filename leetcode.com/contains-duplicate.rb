# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
    counter = Hash.new(0)
    nums.each { |num| 
        counter[num] += 1
        return true if counter[num] > 1
    }

    return false
end