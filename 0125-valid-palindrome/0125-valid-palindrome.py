class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        s=s.lower()
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                a+=i
        return a==a[::-1]