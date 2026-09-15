class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict[int, int](lambda: 0)
        for num in nums:
            counts[num] += 1

        return list(map(lambda pair: pair[0],
                        sorted(counts.items(),
                               key=lambda pair: -pair[1])[:k]))