class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sequences = dict[int, int]()
        for num in nums_set:
            if num - 1 not in nums_set:
                end = num
                while end + 1 in nums_set:
                    end += 1
                sequences[num] = end - num + 1
        return max(sequences.values(), default=0)
