class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        M=max(nums)
        if (len(nums)>M):
            return(M+1)
        else:
            for i in range(0,M):
                if i not in nums:
                    return i