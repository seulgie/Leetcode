class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for c in nums:
            counts[c] += 1
        
        answers = [k for k, v in counts.items() if v == 1]
        
        if answers:
            return max(answers)
        else:
            return -1
