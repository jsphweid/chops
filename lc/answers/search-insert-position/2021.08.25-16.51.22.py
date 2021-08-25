"""
What makes this hard is `You must write an algorithm with `O(log n)` runtime complexity.`
This basically means we need binary search here since scanning the entire list (worst
case)is O(n).

I've never made a binary search algorithm before but I think it relies on finding halfway
points in a sorted list. The basic gist is, given an array in ascending order and the length
of that array, start by finding the middle index by using len//2. If the value at that location
is smaller than what we're comparing, we need to go right. If it's larger, we need to go left.
If it's the same, we found the spot!

If we need to go either right or left, then we use the same algorithm but instead of len//2,
it's current position//2 if left, else len-currentposition//2 if right.

So let's prove that out:

*given:
arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
if we wanted to find value 2, we'd go to len//2 = index 5. Since arr[5] is 10 and that is
greater than 2, we want to go left. 5//2 => 2. arr[2] = value 4. Since that's higher
we go left again. 2//2 = index 1. arr[1] = value 2, which is what we want we return

*if the value we were searching for is 3...
we'd get to arr[1] = value 2. this is too small. we need to go right.

This is where I'm learning my algorithm doesn't make sense. Intuitively I know we want to
go up just a little bit. len-currentposition//2 is incorrect. What we really want is the midpoint
between the last and current position. So we were at index 3. Then 2. So we need 2.5, but since
that's not possible, we should just add 1 to the index and call it a day as far as this algorithm
is concerned, since that's the index where we 'would' place it.

But it's still a little fuzzy to me. I need more examples.

*if the value we're searching for is 9/
We do len//2 which gets us to index 5, value 10. This is less than 10, so we need to descend.
currentposition//2 = index 2, value 4. We need to go up. We use previous+current//2 (5+2//2) which
is position 3 or value 6. 6 is still less than 9. So we need to go up again. previous+current//2
(2+3//2) which is position 2 value 4. Uh oh. This is incorrect. We need to keep going up, not back down.
The "mid-point" of the last two points doesn't quite get us there.

What we need are pillars that persist beyond iterations or something. Like 0 and len(list) are pillars
but we should be able to adjust them sometimes.

In the last example, once we determined it's below the midpoint, we need the top pillar to now be
len(list)/2.

low_pillar=0
high_pillar=len(list) (or maybe len(list) - 1?? probably not)

If the target is above, we can move our low_pillar to the current point
If the target is below, we can move our high_pillar to the current point

This seems like a more coherent approach

So going back to `arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]` and target = 9
midpoint is index 5 value 10. Since target is below, we set high_pillar to current, index 5
midpoint is now index 2 value 4. Target is above, set low_pillar to current.
midpoint is now index 3 value 6. Target is above, set low_pillar to current.
midpoint is now index 4 value 8. Target is above, set low_pillar to current.
midpoint is still index 4 value. At this point, since it's the same as last, we should add 1
and call it a day.

Let's implement this and see what happens.


"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # special condition, should work because len of nums should always be at least 1
        if target < nums[0]:
            return 0

        low_pillar = 0
        high_pillar = len(nums)
        current_index = (high_pillar + low_pillar) // 2
        last_index = None

        # there are two conditions to finishing...
            # 1. it's "stuck" (last index == current index), return current_index + 1
            # 2. it's found the value, return current_index
        while nums[current_index] != target and current_index != last_index:
            if target < nums[current_index]:
                high_pillar = current_index
            else:
                low_pillar = current_index

            # update indices
            last_index = current_index
            current_index = (high_pillar + low_pillar) // 2

        return current_index + 1 if current_index == last_index else current_index


        # does it work for `arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]`
        # yes
        # does it work for their cases? 
        # [1,3,5,6], target = 5, shouldn't even go in while, should work
        # [1,3,5,6], target = 2, should work
        # [1,3,5,6], target = 7, should work
        # [1,3,5,6], target = 0, WILL FAIL, it would return 1... I'll add special condition
        # [1], target = 0, WILL FAIL, but special condition will solve it too

        # submission failed... [1,3,5,6] returns index 3 instead of index 2...
        # My issue was the while loop... should've been an `or` instead of an `and` YIKES


"""
retro, this took me a while as evidenced by all the comments, but I pretty much nailed it the first
time EXCEPT FOR THE OR->AND ISSUE :(
"""




        