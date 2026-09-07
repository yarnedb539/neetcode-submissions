class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        candidate = 0
        for i in nums:
            if not votes:
                candidate = i
                votes += 1
            if votes and candidate != i:
                votes -= 1
            if votes and candidate == i:
                votes += 1
        return candidate