class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = 0
        checked = []
        for i in nums:
            if i not in checked:
                checked.append(i)
            else:
                duplicates += 1
        return bool(duplicates)