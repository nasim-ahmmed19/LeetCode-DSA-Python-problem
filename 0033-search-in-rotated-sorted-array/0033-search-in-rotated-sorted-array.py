class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lb=-1
        n=len(nums)
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                lb=mid
                return lb
            elif nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return lb
        