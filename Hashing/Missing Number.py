class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)  + 1
        dict = {i:0 for i in range(n)}
        
        for k, v in dict.items(): 
            if k not in set(nums):
                return k
