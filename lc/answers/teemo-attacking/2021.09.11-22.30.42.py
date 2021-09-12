"""
brute force method here is to iterate over each time series and add relevant durations to a set 
then return the length of the set

```
times = set()
for t in timeSeries:
    times = times.union(set(range(t, t + duration)))
return len(times)

my next idea keeps in mind that all we need is a total count and doesn't bother with saving 
anything more than that

Let's just iterate over each timeSeries [1, 4] and add duration each time to a sum.
But if we are on a timeSeries that overlaps with the last, we'll just subtract a bit to adjust...
```

the problem is that this times out...

"""

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        lastNum = None
        for t in timeSeries:
            total += duration
            if lastNum and (lastNum + duration) > t:
                total -= (lastNum + duration - t)
            lastNum = t
        return total