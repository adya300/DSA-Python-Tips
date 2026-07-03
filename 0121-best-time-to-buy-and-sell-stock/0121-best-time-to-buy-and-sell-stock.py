class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            l=[]
            m=prices[0]
            profit=0
            for i in prices:
                    if i<m:
                        l.append(profit)
                        m=i
                    else:
                        if i-m>profit:
                            profit=i-m
            l.append(profit)
            return max(l)
