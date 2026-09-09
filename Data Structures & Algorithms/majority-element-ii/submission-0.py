from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = []
        n = len(nums)
        threshold = n // 3
        for num in counter:
            if counter[num] > threshold:
                res.append(num)
        
        return res