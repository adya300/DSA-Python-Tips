class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(set(arr))

        rank = {}
        for i, num in enumerate(a):
            rank[num] = i + 1

        result = []
        for num in arr:
            result.append(rank[num])

        return result