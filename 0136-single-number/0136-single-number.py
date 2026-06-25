class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        d={}
        for i,v in enumerate(nums):
            if v not in d:
                d[v]=1
            else:
                d[v]+=1
            if d[v]==2:
                d.pop(v)
        for k,v in d.items():
            return k