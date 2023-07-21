from typing import List
class Solution:
    def productExceptSelf (self, num: List[int]) -> List[int]:
        res = [1]*(len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=num[i]
            postfix=1
            for i in range(len(nums)-1,-1,-1):
                res[i]*=postfix
                postfix=nums[i]
                return res