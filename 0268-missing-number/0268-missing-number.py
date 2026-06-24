class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        M=max(nums)
        if (len(nums)>M):
            return(M+1)
        else:
            nums.sort()
            count=0
            for num in nums:
                if num != count:
                    return count
                count+=1