class Solution:
    def rotate(self, arr):
        a=arr[-1]
        for i in range(len(arr)-1,0,-1):
            if i==0:
                break
            else:
                arr[i]=arr[i-1]
        arr[0]=a
        return arr
