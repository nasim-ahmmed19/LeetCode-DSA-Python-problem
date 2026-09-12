class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        re=[0]*n
        p_indx,n_indx=0,1
        for i in range(0,n):
            if nums[i]>=0:
                re[p_indx]=nums[i]
                p_indx+=2
            else:
                re[n_indx]=nums[i]
                n_indx+=2
        return re

        