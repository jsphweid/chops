class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and year % 4 == 0:
            if year % 400 == 0 or year % 100 != 0:
                return 29
        return month_days[month]
