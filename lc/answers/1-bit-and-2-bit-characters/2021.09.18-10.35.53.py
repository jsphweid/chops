"""
100 -> 10 0, it is True
1110 -> 11 10 it is False
1001010 -> 10 0 10 10 it is False
101011010010 -> 10 10 11 0 10 0 10 False
10000 -> 10 0 0 0 True
110 -> 11 0 True
010 -> 0 10 False

I think we just iterate through the list. If it's a 0, we flip a var to True. If it's a ... wait
we may need a second flag.
maybe a `is_single_zero`
100 -> 
    1 - False since it's not 0

Wait... this is dumb. We just need to figure out if we're in the middle of building a 2 digit num or not
then return what though... we also need to remember what the last one was
so like building=bool, last_was_single=bool

tracing
010 - good
110 - good
"""
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        is_building=False
        last_was_single=False
        for is_one in bits:
            if is_building:
                # definitely done building now
                last_was_single = False
                is_building = False
            else:
                if is_one:
                    is_building = True
                else:
                    last_was_single = True
        return last_was_single
