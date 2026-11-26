from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        need = Counter(t)
        window = defaultdict(int)
        required = len(need)      # distinct chars that must be satisfied
        formed = 0                # how many are currently satisfied

        best_len = float("inf")
        best_l = 0
        l = 0

        for r, c in enumerate(s):
            window[c] += 1
            if c in need and window[c] == need[c]:
                formed += 1

            # window is valid -> shrink from the left as far as possible
            while formed == required:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l

                left = s[l]
                window[left] -= 1
                if left in need and window[left] < need[left]:
                    formed -= 1
                l += 1

        return "" if best_len == float("inf") else s[best_l:best_l + best_len]