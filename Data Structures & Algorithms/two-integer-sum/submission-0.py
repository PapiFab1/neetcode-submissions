class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                targ = nums[i] + nums[j]
                if targ == target:
                    return [i, j]