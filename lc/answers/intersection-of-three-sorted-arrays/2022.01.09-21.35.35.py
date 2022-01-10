class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res, i, j, k = [], 0, 0, 0
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            one, two, three = arr1[i], arr2[j], arr3[k]
            if one == two == three:
                res.append(one)
                i += 1
                j += 1
                k += 1
                continue
            
            highest = max(one, two, three)
            if one != highest: i += 1
            if two != highest: j += 1
            if three != highest: k += 1
        return res