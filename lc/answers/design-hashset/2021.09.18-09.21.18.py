"""
Since it's storying numbers from 0 to 1000000, we could just store it as an array where 
membership is a matter of an index being true (could be false by default). That's insanely 
expensive memory wise though. I have no idea how to build a set without using set()/dict().
We could use a list under the hood but we'd have to scan the entire list to check for membership
which defeats the purpose of a "set".

I'm going to read the solution on this one and maybe implement afterwards.

So a decent hashing function is a modulo operator. I thought we'd have to use something much more complicated
than this. But this makes sense as modulo predictably transforms a number into another number with smaller
space. For example, % 2 will transform everything into one of two buckets. % 3 will split into 3 buckets
and so on. 

The answer said something about using a prime is better because there will be fewer collisions
but I don't immediately understand how that makes sense. Is 701 really that much better than 700? Maybe
I'll think about that later
997
"""

HASH_NUMBER = 997

class MyHashSet:

    def __init__(self):
        self._data = []
        for _ in range(HASH_NUMBER):
            self._data.append([])
        

    def add(self, key: int) -> None:
        bucket_index = key % HASH_NUMBER
        if key not in self._data[bucket_index]:
            self._data[bucket_index].append(key)

    def remove(self, key: int) -> None:
        bucket_index = key % HASH_NUMBER
        if key in self._data[bucket_index]:
            self._data[bucket_index].remove(key)

    def contains(self, key: int) -> bool:
        bucket_index = key % HASH_NUMBER
        return key in self._data[bucket_index]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)