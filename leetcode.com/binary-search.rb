# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search(nums, target)
    left = 0
    right = nums.length - 1

    while left <= right do
        middle = (left + right) / 2

        if nums[middle] == target then
            return middle
        elsif nums[middle] > target then 
            right = middle - 1
        else
            left = middle + 1
        end
    end

    return -1
end s