"""
===== Initial Thoughts =====
tasks = [[1,2],[2,4],[3,2],[4,1]]
[enqueueTimei, processingTimei]]
history = [0,2,3,1]

ondeck=[[4,1,3], [2,4,1]]

shortest processing time, index, enqueueTimei

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

[[1,2],[2,4],[9,2],[15,1]]

sort list - O(nlogn + n)

"""

import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res, staging, time = [], [], 0
        queue = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        queue.sort(reverse=True)

        while True:
            # transfer every thing can into staging
            while queue and queue[-1][0] <= time:
                enqueue_time, processing_time, index = queue.pop()
                heapq.heappush(staging, (processing_time, index, enqueue_time))

            if queue and not staging:
                time = queue[-1][0]

            if not queue and not staging:
                return res

            if staging:
                processing_time, index, enqueue_time = heapq.heappop(staging)
                time += processing_time
                res.append(index)








