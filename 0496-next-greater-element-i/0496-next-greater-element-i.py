class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for i in nums1:
            for j,k in enumerate(nums2):
                if i==k :
                    if (j+1==len(nums2)):
                        r.append(-1)
                    else:
                        flag=0
                        for m in range(j,len(nums2)):
                            if nums2[m]>i:
                                flag=1
                                r.append(nums2[m])
                                break
                        if flag==0:
                            r.append(-1)
        return r
