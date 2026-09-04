class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict[str, int](lambda: 0)
        for c in s:
            counts[c] += 1
        for c in t:
            counts[c] -= 1

        return all(s == 0 for c, s in counts.items())