class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i,v in enumerate(nums):
            xor^=v
        return xor