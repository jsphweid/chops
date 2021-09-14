class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        primes = [7, 11, 13, 17, 19, 23, 29, 31]
        for p in primes:
            if n % p == 0:
                return False

        i = 0
        num = n
        arr_set = {5, 3, 2}
        arr = [5, 3, 2]
        while num not in arr_set:
            if i == 3:
                return False
            if num % arr[i] == 0:
                num = num // arr[i]
                i = 0
            else:
                i += 1
            
        return True