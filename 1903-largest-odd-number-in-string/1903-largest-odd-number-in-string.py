class Solution:
    def largestOddNumber(self, num: str) -> str:
        if len(num)>10**6:
            return ""
        m=""
        result=0
        for i in num:
            m+=i
            if int(i)%2!=0:
                result=m
        if result==0:
            return ""
        else:
            return result
                