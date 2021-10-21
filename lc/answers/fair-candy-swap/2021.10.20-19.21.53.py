"""
=== Brute Force Approach ===
brute force would be to get a sum of each then iterate over each list within the other list and 
and try swapping each combination. If the swaps increase one and decrease the other appropriately
then it must work and the result can be returned.

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

=== Implemented Approach ===
[1,2,5] [2,4]
totals = 8, 6
iterating over one of them ([1, 2, 5]), we can pretend giving up that one from the total. Then we
know what the result would be adding that num to the other side. That is the number we must match.
We can effectively search via set to see if the difference exists on the other side.

for example
let's focus on [1,2,5] -- we'll iterate on that
if we remove 1, we now have 7. The other side has 6+1=7. So we search for a 0. It doesn't exist.
if we remove 2, we now have 6. The other side has 6+2=8. So we search for a 1. It doesn't exist
if we remove 5, we now have 3. The other side has 6+5=11. So we search for a 4. It does exist.

[1,1], [2,2]
remove 1, now we have 1, otherside has 5. we're looking for 2. it exists

[1,2], [2,3]
remove 1, now we have 2, otherside has 6. we're looking for 2. it exists

[2], [1,3]
remove 2, now we have 0, otherside has 6. we're looking for 3. it exists

~~Complexity Analysis
Time - O(n)
Space - O(m)
"""

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)
        bob = set(bobSizes)
        for num in aliceSizes:
            new_alice_total = alice_total - num
            new_bob_total =  bob_total + num
            diff = new_bob_total - new_alice_total
            if diff % 2 == 0:
                looking_for = diff // 2
                if looking_for in bob:
                    return [num, looking_for]

