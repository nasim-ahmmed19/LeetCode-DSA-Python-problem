class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        my_set=set()
        n=len(nums)
        for i in range(0,n):
            my_set.add(nums[i])
        for j in my_set:
            if j-1 not in my_set:
                x=j
                count=1
                while x+1 in my_set:
                    count+=1
                    x+=1
                longest=max(count,longest)
        return longest