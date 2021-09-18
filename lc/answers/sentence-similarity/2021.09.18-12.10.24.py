"""
seems straight forward but because there are more dislikes than likes, I think there are probably some gotchas...

looks like the index of the similarPairs matters -- it has to line up with sentence1/sentence2 index. My initial
thought was to use a mapping but since position matters, we can just use the list index. But we should also note that
the similarPairs may not have anything (or enough) in it, in which case our assertion has to be that they are equal

I failed on the first submission... So what I thought above just isn't correct apparently

```
["an","extraordinary","meal"]
["one","good","dinner"]
[["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
```

Here was my original submission that worked on 75% of the tests
```
        if len(sentence1) != len(sentence2):
            return False
        for i, (left, right) in enumerate(zip(sentence1, sentence2)):
            good_through_pairs = (len(similarPairs) >= i + 1) and similarPairs[i][0] == left and similarPairs[i][1] == right
            good_through_pairs_opposite = (len(similarPairs) >= i + 1) and similarPairs[i][1] == left and similarPairs[i][0] == right
            if not ((left == right) or good_through_pairs or good_through_pairs_opposite):
                return False
        return True
```

Moving forward, I think we use sets here.

missed the next couple because of failing to understand the mapping


"""

from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        associations = defaultdict(set)
        for l, r in similarPairs:
            associations[l].add(r)
            associations[r].add(l)
        for l, r in zip(sentence1, sentence2):
            if l != r and r not in associations[l] and l not in associations[r]:
                return False
        return True