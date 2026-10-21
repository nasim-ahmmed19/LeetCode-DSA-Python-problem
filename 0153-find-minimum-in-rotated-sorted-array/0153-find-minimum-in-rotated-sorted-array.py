class Solution:
    def findMin(self, nums: list[int]) -> int:
        n=len(nums)
        low,high=0,n-1
        soto=float('inf')
        while low<=high:
            mid=(low+high)//2
            if nums[low]==nums[mid]==nums[high]:
                soto=min(nums[low],soto)
                low+=1
                high-=1
                continue
            elif nums[low]<=nums[mid]:
                soto=min(nums[low],soto)
                low=mid+1
            else:
                soto=min(nums[mid],soto)
                high=mid-1
        return soto
        