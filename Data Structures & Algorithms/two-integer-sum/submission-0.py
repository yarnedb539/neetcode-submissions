class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, x in enumerate(nums):
            if target - x not in seen:
                seen[x] = i
            else:
                return [seen[target - x], i]