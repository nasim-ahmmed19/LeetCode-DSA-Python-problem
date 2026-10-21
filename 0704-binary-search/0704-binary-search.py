class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums)
        low,high=0,n-1
        re=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                re=mid
                return re
            if nums[mid]>=target:
                high=mid-1
            else:
                low=mid+1
        return re


            
        