class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        M=max(nums)
        if (len(nums)>M):
            return(M+1)
        else:
            numss=sorted(nums)
            count=0
            for num in numss:
                if num != count:
                    return count
                count+=1