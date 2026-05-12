class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr_cons_array=[]
        sort_list = sorted(nums)
        for number in sort_list:
            longest_cons = [number]
            for i in range(1, len(nums)+1):
                if (number+i) in nums:
                    longest_cons.append(number+i)
                else:
                    break
            if len(longest_cons) > len(curr_cons_array):
                curr_cons_array = longest_cons
            
        return len(curr_cons_array)