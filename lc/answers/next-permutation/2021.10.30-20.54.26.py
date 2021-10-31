"""
===== Initial Thoughts =====


=== Brute Force Approach ===
convert them all to strings, order them with sort. Find the current one in there, increment index
or go to beginning. reverse it to be integers. would need to pad integers so that 1 is 001.

~~Complexity Analysis
Time - O(n) for conversion then n log n for sort... basically it's n log n
Space - 

But it doesn't matter because ```The replacement must be **[in place](http://en.wikipedia.org/wiki/In-
place_algorithm)** and use only constant extra memory.```

=== Implemented Approach ===
the good thing is that it must already be in a permutation that makes sense... well... any permutation makes
sense really, but ...

[1,2,3] -> [1,3,2]
reverses last two

[3,2,1] -> [1,2,3]
swaps last two, first two, then last two again

[1,1,5] -> [1,5,1]
swaps last two

we need more examples...

[1, 2, 3, 4]
[1, 2, 4, 3]
[1, 3, 2, 4]
[1, 3, 4, 2] ---
[1, 4, 2, 3]
[1, 4, 3, 2]
[2, 1, 3, 4]
[2, 1, 4, 3]
[2, 3, 1, 4]
[2, 3, 4, 1]
[2, 4, 1, 3]
[...]
[4, 3, 2, 1]
[1, 2, 3, 4]... so if it's already the highest, reseting is just reversing really

has something to do with finding the max number
if it's at the end, it seems to unquestionably just swap with the adjacent number
if it's 2nd from the end, it seems to swap with the bigger adjacent number
if it's 3rd over, it may not have to move... or it may go to beginning

-------- starting over

[1,2,4,3]
[1,3,2,4]

find biggest, is there anything to the right that is larger, if not swap largest with neighbor?

the problem is whatever process needs to repeat many times

--------

I want to look at the answer but I shouldn't. Because I know how to solve this in my head, or  on paper...
why can't I automate it with code?

[4,7,2,2,1,8,9]
I know the second I see 8,9 that the next one is clearly to swap those two and call it a day.

[4,7,2,2,1,9,8]
now I know that I have to use the next number... because 9,8 is in reversed order. I can't do any more with that.
So I consider 1,9,8... Since 1 is less than 9, I definitely know it's not in reversed order. If it were in reversed
order, the 1 would have to be greater than or equal to 9.

So once we're on 1, which is less than 9... The next step is to replace it with the next largest and then
rearrange everything after it from lowest to highest.
1,9,8 becomes 8 then 1,9 (1,9, i.e. lowest to highest)

how do we get the rest in order without storing a bunch of state somehow? (constant time)

for example... we know we need to change that 1 to the next highest, which is a 2
[1,4,3,2] - actual
[2,1,3,4] - desired

[1,4,3,2] - start
[2,4,3,1] - flip -4/-1 (because -1 is next largest)
[2,1,3,4] - flip -3/-1  DONE somehow

let's try...
[2,4,3,1] - start
[3,4,2,1] - flip -4/-2 (because -2 was next largest)
[3,1,2,4] - flip -3/-1 idk why, because that's what the previous did... flipping max/min

let's try
[3,4,2,1] - start
[4,3,2,1] - flip -4/-3 (because -3 was next largest)
[4,1,2,3] - flip -3/-1 again...

Question is why do we stop at -2 index...?
it's not quite clear... we need a longer example

[1,5,7,8,3,7,5,4,2,2,1] breaks at -7 (the 3)... next highest is 4, index=-4
[1,5,7,8,4,7,5,3,2,2,1] swap 3/4, index -7/-4
[1,5,7,8,4,1,5,3,2,2,7] swap -6/-1
[1,5,7,8,4,1,2,3,2,5,7] swap -5/-2
[1,5,7,8,4,1,2,2,3,5,7] swap -4/-3

basically you swap then reverse remaining (by also swapping)

TODO: what if multiple next largest??
[1,5,7,8,3,7,5,4,4,2,1] now there are two fours to swap with... which one is better?
let's try left most
[1,5,7,8,4,7,5,3,4,2,1] breaks at -7 (the 3)... next highest is 4, index=-4 (left)
[1,5,7,8,4,1,5,3,4,2,7] swap -6/-1
[1,5,7,8,4,1,2,3,4,5,7] swap -5/-2
[1,5,7,8,4,1,2,4,3,5,7] swap -4/-3 (FAILS)

[1,5,7,8,3,7,5,4,4,2,1]
[1,5,7,8,4,7,5,4,3,2,1] breaks at -7 (the 3)... next highest is 4, index=-3 (right)
[1,5,7,8,4,1,5,4,3,2,7] swap -6/-1
[1,5,7,8,4,1,2,4,3,5,7] swap -5/-2
[1,5,7,8,4,1,2,3,4,5,7] swap -4/-3 WORKS

So it follows we should find the next largest starting from the end of list... and keep the first
one that beats the previous winner (the one that is closest to the breaking number)

does this work on smaller ones?
[3,4,2,1] breaking is -4
[4,3,2,1] breaks at 3, i.e. index -4, next highest is 4 (-3 index)
[4,1,2,3] swap -3/-1... and we're done since we can't go any further...

SOOOOOOOOOoooooo.. it almost worked first try... failed on 

[2,3,1,3,3]

I suspected there might be a problem with these sorts of edge cases.

my algorithm swaps with the FIRST one if there is a tie. It seemed to be the one that actually worked above...

[2,3,1,3,3]

hmm.... what if it were longer

[2,3,1,3,3,3,3]
what is the real next permutation...?
[1,3,3,3,3]

this is the correct order
[3,1,3,3,3]
[3,3,1,3,3]
[3,3,3,1,3]
[3,3,3,3,1]

Where exactly is the incorrect code in my implementation?
my reversal algorithm assumes that everything is in reversed order after swap...

for example
[1,5,7,8,3,7,5,4,2,2,1]
after we swap 3<>4
[1,5,7,8,4,7,5,3,2,2,1]
the remaining list 7,5,3,2,2,1 is all ready to be reversed

so with [2,3,1,3,3]... after we swap...
we have [2,3,3,3,1]... [3,1] is in reverse order... so I'm not immediately sure what the issue is

[3,1,3,3,3], breaking index is 1... best candidate is index 4
[3,3,3,3,1], now reverse start with i,j=2,4

I realized that I had a bug in my code. When choosing the swap candidates, I was missing a condition... we initialize the 
swap candidate with a good choice. We can get a better choice if:
    1. we find a num that is closer
    2. we find a num that is the same value but greater index (further towards the right)
I didn't really have #2 there...

~~Complexity Analysis
Time - O(n) (really like 2n or 3n... one to find breaking, one to find next largest, then one to swap remaining)
Space - O(1)
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1: return

        start_reverse_index = 0

        # find breaking number
        for i in range(len(nums) - 2, -1, -1):  # start second from last
            if nums[i] < nums[i + 1]:
                breaking_num = nums[i]
                breaking_num_index = i
                best_swap_candidate = nums[i + 1]
                best_swap_candidate_index = i + 1
                # see if we can't find a better candidate...
                for j in range(len(nums) - 1, breaking_num_index, -1):
                    if nums[j] > breaking_num and (nums[j] < best_swap_candidate or (nums[j] == best_swap_candidate and j > best_swap_candidate_index)):
                        best_swap_candidate = nums[j]
                        best_swap_candidate_index = j
                # swap with best candidate
                nums[breaking_num_index] = best_swap_candidate
                nums[best_swap_candidate_index] = breaking_num
                start_reverse_index = breaking_num_index + 1
                break  # don't need to go any further

        # reverse everything else... by swapping...
        i, j = start_reverse_index, len(nums) - 1
        while i < j:
            j_num = nums[j]
            nums[j] = nums[i]
            nums[i] = j_num
            i += 1
            j -= 1

        