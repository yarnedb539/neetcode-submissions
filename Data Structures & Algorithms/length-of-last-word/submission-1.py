class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        i = -1
        for i in range(-1, -(len(words)+1), -1):
            if words[i] != "":
                return len(words[i])