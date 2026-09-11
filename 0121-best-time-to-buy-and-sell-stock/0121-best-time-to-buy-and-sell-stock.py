class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p=float('inf')
        max_p=0
        n=len(prices)
        for i in range(0,n):
            min_p=min(min_p,prices[i])
            max_p=max(max_p,prices[i]-min_p)
        return max_p
 
        