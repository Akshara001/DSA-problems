from typing import List
class Solution:
 def twoSum(self,num:List[int],target:int) -> int:
  prevMap ={} #val:index
  for i,n in enumerate (nums):
    diff = target - n
    if diff in prevMap:
        return [prevMap[diff], i]
    prevMap=i
  return
