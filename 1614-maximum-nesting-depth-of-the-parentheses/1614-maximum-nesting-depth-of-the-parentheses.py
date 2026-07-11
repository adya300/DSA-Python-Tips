class Solution:
    def maxDepth(self, s: str) -> int:
        a=0
        f=0
        for i in s:
            if i=="(":
                a+=1
            elif i==")":
                a-=1
            if a>f:
                f=a
        return f