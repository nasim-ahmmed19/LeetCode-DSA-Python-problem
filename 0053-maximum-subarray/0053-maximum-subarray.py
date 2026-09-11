class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=0
        max_to=float('-inf')
        n=len(nums)
        for i in range(0,n):
            total=total+nums[i]
            max_to=max(total,max_to)
            if total<0:
                total=0
        return max_to
