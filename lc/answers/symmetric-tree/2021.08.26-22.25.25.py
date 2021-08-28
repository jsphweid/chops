"""
I feel like is identical to the same-tree problem in the sense that we could easily have used that method
and passed in the node.left as arg1 and node.right as arg2 here. That would be an easy way to solve this.
Is there a better way though?

Actually that doesn't work because the subtrees are still mirrored themselves which means they don't look
identical to each other.

Maybe a better approach is -> how do we recurse through this function (since we know recursion is simple
to implement in trees). We'd have to ask ourselves how does `isSymmetric` apply to branches of the tree.
On the surface, this isn't as simple as applying `isSymmetric` to the branches recursively. There has to
be this top level symmetric concept that would otherwise be destroyed at the branch level.

Maybe there is a clever way to cross wires such that it bends the problem into behaving like a problem
we've solved? Not sure on this yet...

We could invert one tree then see if it's equal to the other, but that seems rather inefficient.

We could do an inorder traversal and assert the values "look a certain way". This method seems easily
achievable. For example, inorder traversal might yield `[1,2,2,3,4,4,3]` There is an obvious structure
here. It's length should always a length like 2^0 + 2^1 + 2^2 where each `+` is a 'maybe'. This can easily
be seen if we break up the list like -> [1] + [2, 2] + [3, 4, 4, 3]. If we break it up that way, then it's
obvious where the pattern goes... It feels like this could be solved more efficiently, but I think this
approach is decent for a first pass.

So...
        # perform inorder traversal to yield an int list
        # use a while loop which increments over 1, 2, 4, etc.
        # if we passed the value without landing exactly on it,
        # it's an automatic false
        # while we're doing that, we should be looking at the last n elements
        # from the 1, 2, 4, etc. seeing if THOSE lists are symmetrical

BUT!!!! I stumbled on another traversal algorithm that is simpler (TODO: is that right?) and makes the 
end comparison easier. We take the first example image and turn it into `[3, 2, 4, 1, 4, 2, 3]` and 
assert that it is equal to it's reversed counterpart. That is all!
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict

class Unit:
    def __init__(self, node: Optional[TreeNode], rank: int):
        self.node = node
        self.rank = rank

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        d = defaultdict(list)
        units_to_process = [Unit(root, 0)]
        while len(units_to_process):
            unit = units_to_process.pop(0)
            node = unit.node
            d[unit.rank].append(node.val if node else None)
            if node:
                next_rank = unit.rank + 1
                units_to_process.extend([Unit(node.left, next_rank), Unit(node.right, next_rank)])

        for values in d.values():
            if values != list(reversed(values)):
                return False

        return True

        """
        Let's explore that... ([] + [3] + [] + [2] + [] + [4] + [] + [1] + [] + [4] + [] + [2] + [] + [3] + []) 3,2,4,1,4,2,3
        Feeling fairly confident about this...

        It failed...

        Thinking through the second example just in case anything comes up...
        [] + [2] + [] + [3] + [] + [1] + [] + [2] + [] + [3] + [] => 2,3,1,2,3... This makes sense to be False

        I don't immediately understand where it's failing. I refactored some variable names, but time to look at the
        error message.

        Seeing the error message: the one that failed was [1, 2, 2, 2, null, 2]
        This looks like
            1
         2     2
        2 n   2
        Why would that pass with True?
        Turns out this evaluates to [] + [2] + [] + [2] + [] + [] + [] + [1] + [] + [2] + [] + [2] + [], 2,2,1,2,2
        So my approach makes it seem symmetrical! Dangit!

        We need to add those Nones in there somehow... Maybe we could simply do `return [None]` `if not r`

        So it appears we aren't incorporating a difference in values between a single child node being None vs.
        both children being None. The difference is actually important here for symmetry.

        After doing that with a hack, it still failed on `[5,4,1,null,1,null,4,2,null,2,null]`
                      5
                4           1
              z   1       z   4   
                 2 z         2 z
        [2] + [n]  + [n] + [4] + [2] + [1] + [n] + [5] + [n] + [1] + [4]
        2,n,n,4,2,1,n,5,n,1,4... it's not symmetrical... why is it returning True?

        I'm at the point where I need to print something out... It's only failing one of 197 test cases... lol.
        This is what that printed...
        `traversed ['z', 4, 2, 1, 'z', 5, 'z', 1, 2, 4, 'z']`

        So my algorithm just simply seems to break down in this case. What a well designed case!

        We need to switch algorithms or embed positions somehow.

        My algorithm I thought would be simpler because it encodes a global left to right ordering but it's not a true inorder
        left to right layer by layer. I just implemented that earlier today, I can't believe I can't rememebr how to do that.
        Or maybe the problem was a bit different?
        
        Honestly, actually what if we stick with it put encode characters where there are empty spaces
                      5
                4           1
              z   1       z   4   
             q q 2 z     q q 2 z

                      5
                4           1
                  1           4
                 2           2

        traversed ['z', 4, 'q', 'a', 'q', 2, 'q', 'a', 'q', 1, 'z', 5, 'z', 1, 'q', 'a', 'q', 2, 'q', 'a', 'q', 4, 'z']

        here is my ridiculous failing solution
        def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def _traversal(r):
            if not r:
                return ["q", "a", "q"]
            if not r.left and not r.right:
                return ["q", r.val, "q"]
            if r.left and not r.right:
                return _traversal(r.left) + [r.val, "z"]
            if not r.left and r.right:
                return ["z", r.val] + _traversal(r.right)
            return _traversal(r.left) + [r.val] + _traversal(r.right)

        traversed = _traversal(root)
        print('traversed', traversed)

        return traversed == list(reversed(traversed))

        I can't understand why this produces the output that it produces and doesn't correctly offset the tree enough.
        So adding garbage characters doesn't fix the problem; the places they get added don't make the false
        symmetry go away. Why? I don't know. I might figure this out later.

        I have to go to bed...

        ...Ok it's the next day magically... still thinking about this problem. I thinking going with the initial
        top-down approach might work. I think it may be simple to do iteratively... we're just solving one layer
        at a time...

        I stared at a piece of paper for 30 minutes and came up with this approach:
        make an array of nodes to process. At the top, there will be only 1. Process that one by putting it's value
        on some return array. Then look at left and right nodes. If one or both are there, add it to the array to
        process. Go until everything is gone from the array.

        """





        