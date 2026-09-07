class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = dict()
        for char in s:
            if char not in count_s:
                count_s[char] = 1
            else:
                count_s[char] += 1
        
        #check for t
        for char in t:
            if char not in count_s or count_s[char]==0:
                return False
            count_s[char] -= 1
        
        for char in count_s:
            if count_s[char] != 0:
                return False

        return True