months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def build_start_map(lst):
    total = 0
    res = {}
    for i, val in enumerate(lst):
        res[i + 1] = total
        total += val
    return res

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split("-")
        year_num, month_num, day_num = int(year), int(month), int(day)
        is_leap = year_num % 4 == 0 and year != "1900"
        months_start = build_start_map(months)
        months_start_leap = build_start_map(months_leap)
        count = months_start_leap[month_num] if is_leap else months_start[month_num]
        return count + day_num
