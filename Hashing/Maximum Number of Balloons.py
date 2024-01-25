class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)            
        
        bCount = c['b']
        aCount = c['a']
        lCount = c['l'] // 2
        oCount = c['o'] // 2
        nCount = c['n']
        
        return min(bCount, aCount, lCount, oCount, nCount)
