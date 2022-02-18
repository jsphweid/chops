class Solution:
    def average(self, salary: List[int]) -> float:
        low, high, total = float("inf"), -float("inf"), 0
        for s in salary:
            total += s
            low = min(low, s)
            high = max(high, s)
        return (total - high - low) / (len(salary)  - 2)