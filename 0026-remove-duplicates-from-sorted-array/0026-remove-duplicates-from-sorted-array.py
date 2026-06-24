class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic={}
        n_s=sorted(nums)
        for i,v in enumerate(nums):
            if v not in dic:
                dic[v]=1
            else:
                dic[v]+=1
        nums[:]=dic.keys()

