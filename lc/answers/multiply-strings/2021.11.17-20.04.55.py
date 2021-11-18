"""
  123
  456
x____
  738
 6150
49200
+____
56088

top=3 bottom=6 carry=1 remainder=8 num=8   i=1 (at end)
top=2 bottom=6 carry=1 remainder=3 num=38  i=2 (at end)
top=1 bottom=6 carry=0 remainder=7 num=700 i=3 (at end)

num1=2 num2=3
carry=0 num=0 i=0 
top=3 bottom=2 carry=0, remainder=6

"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        results = []
        for i, char1 in enumerate(num2[::-1]):
            carry = 0
            num = 0
            for char2 in num1[::-1]:
                top, bottom = int(char2), int(char1)
                carry, remainder = divmod(top * bottom + carry, 10)
                num += (remainder * (10 ** i))
                i += 1
            num += (carry * (10 ** i)) if carry else 0
            results.append(num)
        return str(sum(results))
        