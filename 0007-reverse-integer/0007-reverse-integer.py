class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            a=str(x)
            a=a[1:]
            a=int(a[::-1])
            if a<(-2)**31 or a>2**31:
                return 0
            else:
                return -a
        else:
            a=int(str(x)[::-1])
            if a<(-2)**31 or a>2**31:
                return 0
            else:
                return a