
import heapq
from collections import defaultdict


class MedianWindow:
    def __init__(self):
        self.small = []
        self.large = []
        self.delayed = defaultdict(int)

        self.small_size = 0
        self.large_size = 0
        self.small_sum = 0
        self.large_sum = 0

    def prune(self, heap, is_small):
        while heap:
            num = -heap[0] if is_small else heap[0]

            if self.delayed[num] == 0:
                break

            self.delayed[num] -= 1
            if self.delayed[num] == 0:
                del self.delayed[num]

            heapq.heappop(heap)

    def rebalance(self):
        self.prune(self.small, True)
        self.prune(self.large, False)

        if self.small_size > self.large_size + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

            self.small_size -= 1
            self.large_size += 1
            self.small_sum -= value
            self.large_sum += value

            self.prune(self.small, True)

        elif self.small_size < self.large_size:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

            self.large_size -= 1
            self.small_size += 1
            self.large_sum -= value
            self.small_sum += value

            self.prune(self.large, False)

    def add(self, num):
        self.prune(self.small, True)

        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
            self.small_sum += num
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
            self.large_sum += num

        self.rebalance()

    def remove(self, num):
        self.prune(self.small, True)
        self.prune(self.large, False)

        self.delayed[num] += 1

        if num <= -self.small[0]:
            self.small_size -= 1
            self.small_sum -= num

            if num == -self.small[0]:
                self.prune(self.small, True)
        else:
            self.large_size -= 1
            self.large_sum -= num

            if self.large and num == self.large[0]:
                self.prune(self.large, False)

        self.rebalance()

    def get_cost(self):
        median = -self.small[0]

        left = median * self.small_size - self.small_sum
        right = self.large_sum - median * self.large_size

        return left + right


class Solution(object):
    def minOperations(self, nums, x, k):
        n = len(nums)

        if k == 0:
            return 0

        if k * x > n:
            return -1

        # Calculate cost of every size-x window
        window = MedianWindow()
        costs = []

        for i in range(x):
            window.add(nums[i])

        costs.append(window.get_cost())

        for i in range(x, n):
            window.remove(nums[i - x])
            window.add(nums[i])
            costs.append(window.get_cost())

        # Dynamic Programming
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    cost = prev[i - x] + costs[i - x]
                    curr[i] = min(curr[i], cost)

            prev = curr

        return prev[n]