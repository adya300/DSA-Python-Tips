class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_z=[]
        z=[]
        for i in nums:
            if i == 0:
                z.append(0)
            else:
                non_z.append(i)
        nums[:]=non_z[:]+z[:]