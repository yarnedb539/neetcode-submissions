class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        best = 1
        curr = 1
        last_seen = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == (last_seen + 1):
                curr += 1
            else:
                if curr > best:
                    best = curr
                curr = 1
            last_seen = nums[i]
        return max(best, curr)