class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list_len = len(nums)
        output = []

        for i in range(list_len):
            for j in range(list_len):
                for k in range(list_len):
                    if (k != j) and (k != i) and (j != i):
                        if (nums[i] + nums[j] + nums[k]) == 0:
                            if len(output) == 0:
                                output.append(sorted([nums[i], nums[j], nums[k]]))
                            else:
                                if sorted([nums[i], nums[j], nums[k]]) not in output:
                                    output.append(sorted([nums[i], nums[j], nums[k]]))
        return output