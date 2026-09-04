class Solution:
    @staticmethod
    def count(s: str):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict[tuple[int], list[str]](list)
        for s in strs:
            anagrams[self.count(s)].append(s)
        return list(anagrams.values())
