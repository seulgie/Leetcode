class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # initial sum of first k values in num
        max = now = sum(nums[:k])
        for i in range(k, len(nums)):
            # update sliding window sum k
            now += nums[i] - nums[i-k]
            if now > max:
                max = now

        return max/k
        
