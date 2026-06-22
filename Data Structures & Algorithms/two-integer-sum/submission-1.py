class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap = {i: target - num for i, num in enumerate(nums)}
        # for key, val in hashmap.items():
        #     if val in nums:
        #         return [key, nums.index(val)]

        hmap = {}

        for i, n in enumerate(nums):
            if target - n in hmap:
                return [hmap[target - n], i]
            hmap[n] = i