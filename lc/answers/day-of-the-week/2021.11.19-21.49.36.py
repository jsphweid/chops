"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

def days_since_beginning(day: int, month: int, year: int):
    years_days_passed = (year - 1971) * 365
    month_days_passed = sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month - 1])
    days_passed = day - 1
    subtotal = years_days_passed + month_days_passed + days_passed

    # adjust for leap years...
    # 2000 was a leap year but 2100 isn't
    current_year_is_leap = year % 4 == 0 and year != 2100
    leap_years = set(range(1972, 2100, 4))
    num_leap_years = len([y for y in range(1971, year) if y in leap_years])
    is_feb_29 = month == 2 and day == 29
    past_feb_28 = month > 2 or is_feb_29
    num_leap_years = num_leap_years + 1 if current_year_is_leap and past_feb_28 else num_leap_years
    return subtotal + num_leap_years - is_feb_29

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # jan 1 1971 was a friday
        days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

        # how many days have passed since then?
        passed = days_since_beginning(day, month, year)
        return days[passed % 7]
        