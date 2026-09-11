class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(0,len(nums)):
            deff=target-nums[i]
            if deff in hashmap:
                return [hashmap[deff],i]
            hashmap[nums[i]]=i

        