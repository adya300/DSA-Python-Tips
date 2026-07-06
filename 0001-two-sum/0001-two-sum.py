class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            need=target-v
            for j,k in enumerate(nums):
                if j==i:
                    continue
                elif k==need:
                    return [i,j]
        else:
            return []