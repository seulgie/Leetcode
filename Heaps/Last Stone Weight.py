class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            for stone in stones:
                first = abs(heapq.heappop(stones))
                second = abs(heapq.heappop(stones))
                if first != second:
                    heapq.heappush(stones, -abs(first-second))

        return abs(stones[0]) if stones else 0
        
