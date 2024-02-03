class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            # the smallest get popped immediately
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        # push new val into the heap
        heapq.heappush(self.heap, val)
        # pop small values in ascending order until len(heap) becomees k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
