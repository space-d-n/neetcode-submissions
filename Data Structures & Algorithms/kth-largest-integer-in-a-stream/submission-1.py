class KthLargest:

    import heapq

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums) if nums else []
        self.heap = nums
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        print(self.heap)

        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
