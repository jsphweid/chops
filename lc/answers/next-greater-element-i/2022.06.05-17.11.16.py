class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        val_to_nxt_greater = {}
        stack = []
        for i, n in enumerate(nums2):
            while stack and n > stack[-1]:
                nn = stack.pop()
                val_to_nxt_greater[nn] = n
            stack.append(n)
        return [val_to_nxt_greater.get(n, -1) for n in nums1]
