"""
Failed the first time because the one that works
===== Initial Thoughts =====
~~Complexity Analysis
Time - 
Space - 
"""

def makes_enough(lst, minimum, k):
	chunks_made = 0
	acc = 0
	for num in lst:
		acc += num
		if acc >= minimum:
			chunks_made += 1
			acc = 0
	return chunks_made >= k + 1

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        l, r = 1, sum(sweetness) + 1
        while l < r:
        	mid = (l + r) // 2
        	if makes_enough(sweetness, mid, k):
        		l = mid + 1 # need to go into false conditions, i.e. higher numbers
        	else:
        		r = mid
        return l - 1




