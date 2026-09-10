class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash={}
        n=len(nums)
        for i in range(0,n+1):
            hash[i]=0
        for i in nums:
            hash[i]=1
        for k,v in hash.items():
            if v==0:
                return k
        