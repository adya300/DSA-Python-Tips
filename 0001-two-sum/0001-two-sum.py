class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            for j,k in enumerate(nums):
                if i!=j and v+k==target:
                    return [i,j]