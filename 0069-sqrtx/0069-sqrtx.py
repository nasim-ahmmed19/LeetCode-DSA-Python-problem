class Solution:
    def mySqrt(self, x: int) -> int:
        low,high=0,x//2
        res=1
        if x<2:
            return x
        while low<=high:
            mid=(low+high)//2
            mid_sq=mid*mid
            if mid_sq<=x:
                res=mid
                low=mid+1
            else:
                high=mid-1
        return res





        