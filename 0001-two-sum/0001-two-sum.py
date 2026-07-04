class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      hasmap = {}
      for i,num in enumerate(nums):
        needed = target-num
        if needed in hasmap:
            return hasmap[needed],i

        hasmap[num] = i  