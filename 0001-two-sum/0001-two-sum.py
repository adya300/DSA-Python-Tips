class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
                for m,n in enumerate(nums):
                    if m==i:
                        continue
                    elif v+n==target:
                        return [i,m]