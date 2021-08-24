# this can be done:
# 1. using regex which I don't know off hand
# 2. using trim() for the first and last
# 3. or split on " ", then filtering out garbage, then getting last word
# 4. algorithm that counts backwards until it hits beginning of str or empty space

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # get length
        str_length = len(s)
        # set i to last char
        i = str_length - 1
        # store a count that increments as i decrements each loop
        count = 0
        is_counting = False
        while i >= 0:
            if s[i] == " ":
                if is_counting:
                    break
                else:
                    i = i - 1
                    continue
            else:
                is_counting = True
                count += 1
            i = i - 1
        return count


        # if char is non-space, flip a flag, else skip initially
        # after, stop counting and iterating i is at beginning, or space is hit