from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k, arrival, load):
        num_tasks = [0] * k
        heap = []
        sl = SortedList([i for i in range(k)] + [i+k for i in range(k)])
        for i, (s, t) in enumerate(zip(arrival, load)):
            i %= k
            while heap and heap[0][0] <= s:
                _, j = heapq.heappop(heap)
                sl.add(j)
                sl.add(j+k)
            if len(sl):
                j = sl[sl.bisect_left(i)] % k
                sl.remove(j)
                sl.remove(j+k)
                num_tasks[j] += 1
                heapq.heappush(heap, (s+t, j))
        m = max(num_tasks)
        return [i for i, n in enumerate(num_tasks) if n == m]