class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=len(nums)/3
        d={}
        result=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            if (d[i]>a) and (i not in result):
                    result.append(i)
        return result
            