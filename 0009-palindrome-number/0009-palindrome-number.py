class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        zwe=y[::-1]
        return y==zwe