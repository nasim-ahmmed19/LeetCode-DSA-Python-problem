# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         n=len(nums)
#         k=k%n
#         nums[:]=nums[n-k:]+nums[:n-k]
#         return nums


# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         n=len(nums)
#         k=k%n
#         for _ in range(k):
#             x=nums.pop()
#             nums.insert(0,x)
#         return nums

class Solution:

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1 
      
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
