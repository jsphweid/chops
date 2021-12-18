class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for start, end in zip(startTime, endTime):
            count += start <= queryTime <= end
        return count