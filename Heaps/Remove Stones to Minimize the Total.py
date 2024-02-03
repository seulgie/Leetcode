class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        stones = [-stone for stone in piles]
        heapq.heapify(stones)

        for _ in range(k):
            first = -heapq.heappop(stones)
            remove = first // 2
            heapq.heappush(stones, -(first - remove))

        return -sum(stones)
        
