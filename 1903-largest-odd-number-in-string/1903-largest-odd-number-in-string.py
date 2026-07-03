class Solution:
    def largestOddNumber(self, num: str) -> str:
        m = ""
        result = ""

        for i in num:
            m += i
            if int(i) % 2 != 0:
                result = m

        return result