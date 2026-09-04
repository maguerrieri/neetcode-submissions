class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = dict[int, int]()
        for i, num in enumerate(nums):
            other = target - num
            if other in indices:
                return [indices[other], i]
            else:
                indices[num] = i
        raise ValueError("Precondition not met")