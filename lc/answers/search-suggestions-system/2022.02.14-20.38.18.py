"""
=== Brute Force Approach ===
brute force would be to search through each character of the string
getting all strings from list that start with that substring
then sort them, clip them at 3 and add that item to the list.

n is list length
s is search word length
O(s) to iterate through each char
    O(n) to iterate through all words
        O(s) to check if substring matches (realistically never O(s) really)
    O(nlogn) sort those words

~~Complexity Analysis
Time - O(s(ns + nlogn))
Space - O(s)

We could move the nlogn bit up and it'd be:
O(s^2 n + nlogn) or O(n(s^2 + logn))

=== Implemented Approach ===
better approach is to sort first, then use a trie?

["mobile","moneypot","monitor","mouse","mousepad"]

but also store a ref (index) to the word it matches at each layer
{
    m: {
        matches: [0,1,2,3,4]
        o: {
            matches: [0,1,2,3,4]
            b: {
                matches: [0]
                i: {
                    matches: [0]
                    l: {
                        matches: [0]
                        e: {
                            matches: [0]
                        }
                    }
                }
            }
        }
    }
}

O(nlogn) to sort
O(ns) to fill
O(s) to get final (maybe O(s^2)) because we add the item to the list, actuall no, it's constant 3
so overall... idk how best to describe it.
O(ns) is the bulkiest part

failed once because I didn't consider a case where the search word didn't exist in there.
presumably we should just return empty lists every time

I saw a lee had a binary solution that was compact.
"""
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = {}
        for i, product in enumerate(products):
            curr = trie
            for char in product:
                if char in curr:
                    curr[char]["matches"].append(i)
                else:
                    curr[char] = {"matches": [i]}
                curr = curr[char]

        curr, res = trie, []
        for i, char in enumerate(searchWord):
            arr = []

            if char not in curr:
                res.extend([[]] * (len(searchWord) - i))
                return res

            matches = curr[char]["matches"]
            for j in range(min(3, len(matches))):
                arr.append(products[matches[j]])
            res.append(arr)
            curr = curr[char]
        return res


