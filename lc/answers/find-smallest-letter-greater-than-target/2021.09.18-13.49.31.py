"""
we should just be able to find the next highest and if it doesn't exist, return first element
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]