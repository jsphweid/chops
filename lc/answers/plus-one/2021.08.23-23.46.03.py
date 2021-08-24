# presumably [9, 9] -> [1, 0, 0]
# 1. doing right to left addition with carrying
# 2. use some bit shifting to merge each of these into a number, add 1, then reconstruct the array
# 3. use strings and int parsing to get results

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # join digits together in a string [9, 9] -> "99"
        string = "".join([str(d) for d in digits])
        # convert to integer "99" -> 99
        num = int(string)
        # add one 99 -> 100
        num += 1
        # convert back to string 100 -> "100"
        str_again = str(num)
        # split each digit "100" -> ["1", "0", "0"]
        strs = list(str_again)
        # map over each digit converting it back to an integer [1, 0, 0]
        return [int(s) for s in strs]