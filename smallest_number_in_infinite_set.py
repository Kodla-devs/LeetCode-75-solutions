import heapq


class SmallestInfiniteSet(object):
    def __init__(self):
        self.current = 1
        self.added_back = []  # heap
        self.added_set = set()  # O(1)

    def popSmallest(self):
        if self.added_back and self.added_back[0] < self.current:
            smallest = heapq.heappop(self.added_back)
            self.added_set.remove(smallest)
            return smallest
        else:
            self.current += 1
            return self.current - 1

    def addBack(self, num):
        if num < self.current and num not in self.added_set:
            heapq.heappush(self.added_back, num)
            self.added_set.add(num)
