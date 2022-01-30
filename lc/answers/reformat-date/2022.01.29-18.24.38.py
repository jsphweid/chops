"""
"6th Jun 1933"
day="6th" month="Jun" year="1933"
month="6"
day="6"
"1933-06-06"
"""

class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(" ")
        month = ["-", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(month)
        month = str(month)
        day = "".join([c for c in day if c.isdigit()])
        return f"{year}-{'0' + month if len(month)== 1 else month}-{'0' + day if len(day) == 1 else day}"