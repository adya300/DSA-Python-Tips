class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(list(set(arr)))
        rank={}
        for i,v in enumerate(a):
            rank[v]=i+1
        result=[]
        for i in arr:
            result.append(rank[i])
        return result
