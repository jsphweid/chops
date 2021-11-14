"""
findCircleNum([[1,1,0],[1,1,0],[0,0,1]])

provinces=[]

i=0 found=False

explore_province(0,{0})
    explore_province(1,{0,1})

[{0,1}]
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = []

        def explore_province(i: int, province=set()):
            province.add(i)
            connections = isConnected[i]
            for j, is_connected in enumerate(connections):
                if is_connected and j not in province:
                    explore_province(j, province)
            return province

        for i in range(len(isConnected)):
            found = False
            for province in provinces:
                if i in province:
                    found = True
                    break
            if not found:
                provinces.append(explore_province(i))

        return len(provinces)