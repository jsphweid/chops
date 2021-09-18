"""
binary search for real
"""
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters)
        while low < high:
            mid = (low + high) // 2
            if letters[mid] > target:
                high = mid
            else:
                low = mid + 1
        return letters[low % len(letters)]