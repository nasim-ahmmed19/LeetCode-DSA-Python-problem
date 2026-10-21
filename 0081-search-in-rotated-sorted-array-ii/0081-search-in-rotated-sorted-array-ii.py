class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n=len(nums)
        low,high=0,n-1
        re=False
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                re=True
                return re
            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            elif nums[mid]<=nums[high]:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
        return re
        