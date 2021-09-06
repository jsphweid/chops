"""
the first pass here would be to make a set of nums
then iterate through lower/upper range (inclusive) adding
items to a list which gets added into a larger list when
contiguity is broken. These broken lists are then translated into
ranges

So that solution is very inefficient:
```
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums_set = set(nums)
        final = []
        temp = []
        for num in range(lower, upper + 1):
            if num not in nums_set:
                if not len(temp) or ((num - 1) == temp[-1]):  # it should go in temp
                    temp.append(num)
                else:  # temp is done... reset
                    final.append(temp)
                    temp = [num]
        if len(temp):
            final.append(temp)
        return [f"{item[0]}" if len(item) == 1 else f"{item[0]}->{item[-1]}" for item in final]
```

a much better way would be to just loop over nums creating ranges for each non-contiguous neighbor.

Going back and forth between lower/upper and nums is kind of annoying though, since one is 
inclusive and one is exclusive. A clever idea here would be to include the lower/upper in nums so that
the whole thing can be solved with the same algorithm.

`[0,1,3,50,75], lower = 0, upper = 99`
turns into `[-1,0,1,3,50,75,100]`

how do we make ranges from that?
since we always need to compare it to neighbors we can start on the 1st index and increment to the end
looking for opportunities.
[1, 3] -> create "2"
[3, 50] -> create "4->49"
[50, 75] -> create "51->74"
[75, 100] -> create "76->99"

seems pretty straightforward

"""

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        final_nums = [lower - 1] + nums + [upper + 1]
        ret = []
        for i in range(1, len(final_nums)):
            current_num = final_nums[i]
            previous_num = final_nums[i - 1]
            diff = abs(previous_num - current_num)
            if diff == 1:
                continue
            elif diff == 2:
                ret.append(str(current_num - 1))
            else:
                ret.append(f"{previous_num + 1}->{current_num - 1}")
        return ret


    """
    failed on this edge case [-1] -1, 0
    that makes [-2, -1, 1]
    our diff formula `abs(abs(current_num) - abs(previous_num))` doesn't work here
    diff should never be 0...
    """


