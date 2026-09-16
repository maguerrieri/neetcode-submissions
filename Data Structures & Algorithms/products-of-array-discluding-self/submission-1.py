from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        partials_forward = [1] * len(nums)
        for i, n in islice(enumerate(nums), 0, len(nums) - 1):
            partials_forward[i + 1] = partials_forward[i] * n

        partials_reverse = [1] * len(nums)
        for i, n in islice(reversed(list(enumerate(nums))), 0, len(nums) - 1):
            partials_reverse[i - 1] = partials_reverse[i] * n

        return [before * after
                for before, after
                in zip(partials_forward, partials_reverse)]