"""
===== Initial Thoughts =====
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
it's increasing from the beginning

arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
it's decreasing to end

=== Implemented Approach ===
have a state variable top_found=False. It gets flipped to true when the number starts
decreasing. If the number is ever increasing when top_found=True or when the number
is flat, return False. Else return True

~~Complexity Analysis
Time - O(n)
Space - O(1)

Failed on [0, 3, 2, 1]... my mental tracing didn't work, damn.
3 < 0 => False, top_found=False... continue
2 < 3 => True, top_found=False... go into if statement, flip top_found
1 < 2 => True, top_found=True... continue

seems right... did I forget to save? no it failed again... how did I mess this up.

range is 1 2 3
Actually it looks like we're getting f'ed by order of operations
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[1] < arr[0]: return False
        top_found=False
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                # always exit if it's flat for any reason
                return False

            # increasing -> False, decreasing->True
            if (arr[i] < arr[i - 1]) != top_found:
                # the statement was wrong...
                if top_found:
                    # but we've already flipped it
                    return False
                else:
                    # or we get one chance to fix it...
                    top_found = True
        return top_found