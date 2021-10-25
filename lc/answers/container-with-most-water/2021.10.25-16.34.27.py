class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            current = (right - left) * min(height[left], height[right])
            best = max(best, current)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best