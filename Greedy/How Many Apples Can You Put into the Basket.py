class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        weight.sort()
        cnt = 0
        left_weight = 5000
        
        for apple in weight:            
                left_weight -= apple
                if left_weight < 0: break
                else: cnt += 1
            
        return cnt
        
