class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = defaultdict[str, int](lambda: 0)
        for c in s:
            counts_s[c] += 1
        
        counts_t = defaultdict[str, int](lambda: 0)
        for c in t:
            counts_t[c] += 1

        return counts_s == counts_t