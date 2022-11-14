class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return True

        increasing = None
        i = 1
        while i < len(nums) and nums[0] == nums[i]:
            i += 1

        increasing = nums[i] > nums[0] if i < len(nums) else True
        decreasing = not increasing

        while i < len((nums)):
            if increasing and nums[i] < nums[i - 1]:
                return False
            elif decreasing and nums[i] > nums[i - 1]:
                return False
            i += 1
            
        return True