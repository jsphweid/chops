class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest = (-float("inf"), "a")
        for i in range(len(releaseTimes)):
            pressed = 0 if i == 0 else releaseTimes[i - 1]
            duration = releaseTimes[i] - pressed
            longest = max(longest, (duration, keysPressed[i]))
        return longest[1]
