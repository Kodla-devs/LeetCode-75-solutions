import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)
        
        return heap[0]
