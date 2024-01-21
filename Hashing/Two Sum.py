class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in dict:
                return [i, dict[rest]]

            dict[nums[i]] = i
