class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ds = dict()
        dt = dict()

        for char in s:
            if char not in ds:
                ds[char] = 0
            ds[char] += 1
        
        for char in t:
            if char not in dt:
                dt[char] = 0
            dt[char] += 1

        for char in ds:
            if ds.get(char) != dt.get(char):
                return False
        return True