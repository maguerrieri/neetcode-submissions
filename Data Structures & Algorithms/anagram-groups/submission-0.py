class Solution:
    @staticmethod
    def frozen(counts: Counter):
        return frozenset(counts.items())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict[frozenset[tuple[str, int]],
                               list[str]](list)
        for s in strs:
            anagrams[self.frozen(Counter(s))].append(s)
        return list(anagrams.values())
