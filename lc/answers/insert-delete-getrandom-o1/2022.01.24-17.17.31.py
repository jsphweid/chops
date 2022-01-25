"""
===== Initial Thoughts =====
why not just use a list as the main struct and use a set to check only for duplicates?
removing would be O(n) though

looks like for a set 'average' case deletion is O(1)

if we only use a set, we can't convert it to a list then pick a random item because that's
going to be O(n).

Since it's only ints, maybe we can design our own?

Maybe we can optimize for `getRandom` being called many times after a single insert?

what we have so far:
we can make average case for deletion O(1) but getRandom is hard then
    - how do you pick a random item from a set in O(1) time?
we can make getRandom easy but deletion O(1) becomes hard.

I'm not sure I understand the nuances of `average` good enough to know what I can get away with.

I think I'm going to have to read the discussions.

Read an answer that was really clever... just keep track of inserted positions and when you remove, 
just delete the item from the list by swapping the last item in the list to that position. then delete
the last item (which is a O(1) operation)
"""

import random

class RandomizedSet:

    def __init__(self):
        self.items = []
        self.order = {}

    def insert(self, val: int) -> bool:
        if val not in self.order:
            self.order[val] = len(self.items)
            self.items.append(val)
            return True
        return False

        """
remove 0
insert 2
remove 1
[1]
{0:0, 1:1}
        """

    def remove(self, val: int) -> bool:
        if val in self.order:
            if self.items[-1] == val:
                self.items.pop()
            else:
                self.items[self.order[val]] = self.items[-1]
                self.order[self.items[-1]] = self.order[val]
                self.items.pop()
            del self.order[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return self.items[random.randint(0, len(self.items) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()