class Solution:
    def lowerBound(self,nums,target):
        n=len(nums)
        low,high=0,n-1
        lb=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
    
    def upperBound(self,nums,target):
        n=len(nums)
        low,high=0,n-1
        up=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                up=mid
                high=mid-1
            else:
                low=mid+1
        return up
        
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb=self.lowerBound(nums,target)
        up=self.upperBound(nums,target)
        if lb==len(nums) or nums[lb]!=target:
            return [-1,-1]
        return [lb,up-1]

