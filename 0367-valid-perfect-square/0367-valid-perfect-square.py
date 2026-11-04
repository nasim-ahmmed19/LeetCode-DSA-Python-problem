class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low,high=0,num//2
        if num<2:
            return True
        while low<=high:
            mid=(low+high)//2
            m_sq=mid*mid
            if m_sq==num:
                return True
            elif m_sq<num:
                low=mid+1
            else:
                high=mid-1
        return False
        