"""
    123
    456
    x__
    738
   6150
  49200
+______
  56088

654
6, 0, 0
321
 9
 9
81

    123
     56
    x__
    738
   6150
+______
   6888

    98
     9
   x__
   738
  6150
+_____

top=8, remainder=7, num=2
num * 10^0 => 2
top=9 remainder=8 num=8
82
882


    123
    456
    x__
    738
   6150
  49200
+______
  56088

"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = (num1, num2) if len(num1) >= len(num2) else (num2, num1)
        total = 0
        for i, char2 in enumerate(reversed(num2)):
            bottom, remainder, subtotal, j = int(char2), 0, 0, 0
            for char1 in reversed(num1):
                top = int(char1)
                remainder, num = divmod(top * bottom + remainder, 10)
                subtotal += num * 10 ** (j + i)
                j += 1
            if remainder: 
                subtotal += remainder * (10 ** (j+i))
            print('subtotal', subtotal)
            total += subtotal
        return str(total)
