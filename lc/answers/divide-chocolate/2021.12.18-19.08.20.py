"""
===== Initial Thoughts =====
1. 
[1,2,2,1,2,2,1,2,2] = 3 chunks
1 (2 more chunks in 8 sections)
2 (2 more chunks in 7 sections)
3 (2 more chunks in 6 sections)
...
7 (2 more chunks in 2 sections)

1. dfs with backtracking
best = 3
[1,2] [2,1] [2,2,1,2,2]


[1] [2] [2,1,2,2,1,2,2]
[1] [2,2] [1,2,2,1,2,2]
[1] [2,2,1] [2,2,1,2,2]

*** something here
[1,2,2,1,2,2]
[1] [2] [2,1,2,2] => 1
[1,2] [2] [1,2,2] => 2
[1,2,2] [1] [2,2] => 1
[1,2,2,1] [2] [2] => 2


2. 

* slick approach, but really tricky
[1,2,2] [1,2,2] [1,2,2]

[1,2,3] [4,5] [6] [7] [8] [9]

[9] [8] [7] [6,5] [4,3] [2,1]

[9] [8] [4,5] [6] [7] [1,2,3]

{
    0: 9, [9],
    1: 8, [8],
    2: 9, [4,5],
    3: 6, [6],
    4: 7, [7],
    5: 6, [1,2,3]
}

=== Brute Force Approach ===
for above example
nums = [1,2,2,1,2,2,1,2,2]
best = 0
for i in range(len(nums) - 2):
    for j in range(i + 1, len(nums) - 1):
        minimum = min(sum(nums[:i]), sum(nums[i:j]), sum(nums[j:]))
        best = max(best, minimum)


Thinking about efficiency (looks like pascal's triangle)
5 chunks 5 people => 1
5 chunks 4 people => 4
5 chunks 3 people => 6
5 chunks 2 people => 4
5 chunks 1 person => 1

6 chunks 6 people => 1
6 chunks 5 people => 5
6 chunks 4 people => 10
6 chunks 1 person => 1

it times out

Thinking about this again a few weeks later...
[2,3,4,3,2,1,5,7,3,4] k=5 (6) 10 elements, max group size is 5
[14,13,15,18,18,20]
sliding window may help locate where the min would be
[[2,3][4][3,2][1,5][7][3,4]]

[1,2,3,4,5,6,7,8,9] k=5, 6 groups 9 elements. therefore the absolute
biggest any group can be is 4 elements. And the smallest 4 element
sliding window is around [1,2,3,4]. The answer is ultimately [1,2,3]

it's just too fuzzy to get us an actual answer but may point us
in the right direction?


idk how else to think about it... maybe I can just try to optimize my solution somehow

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

[1,2,3,4,5,6,7,8,9]
[1][2][3][4][5][6,7,8,9]
"""


from collections import deque
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        sums, deques = [], []
        for i in range(k + 1):
            deques.append(deque(sweetness[i:] if i == k else [sweetness[i]]))
        for d in deques: sums.append(sum(d))

        best, last = 0, None
        while True:
            minimum = (inf, 0)
            for index, total in enumerate(sums):
                minimum = min(minimum, (total, index))
            worst, min_index = minimum

            if tuple(sums) == last:
                break
            else:
                last = tuple(sums)

            best = max(best, worst)

            # steal from next...
            for index in range(min_index + 1, k + 1):
                num = deques[index].popleft()
                sums[index] -= num
                deques[index - 1].append(num)
                sums[index - 1] += num
                if len(deques[index]) > 0:
                    break
        return best

