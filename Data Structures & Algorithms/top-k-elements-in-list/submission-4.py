class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict[int, int](lambda: 0)
        for num in nums:
            counts[num] += 1

        frequencies = [list[int]() for _ in range(len(nums))]
        for n, c in counts.items():
            frequencies[c - 1].append(n)

        top_k = []
        for n in reversed(frequencies):
            top_k.extend(n)
            if len(top_k) >= k:
                return top_k[:k]
