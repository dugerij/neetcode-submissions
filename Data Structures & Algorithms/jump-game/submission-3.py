class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        i = 0

        while i <= max_reach:
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums):
                return True
            i += 1

        return i == len(nums) 
