"""
[[1,3],[2,2],[3,1]] truckSize=4
num_boxes=1 units_per_box=3 boxes_to_consume=1 truckSize=3 res=3 i=1
num_boxes=2 units_per_box=2 boxes_to_consume=2 truckSize=1 res=7 i=2
num_boxes=3 units_per_box=1 boxes_to_consume=1 truck_size=0 res=8 i=3

failed...


"""

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        res, i = 0, 0
        while truckSize and i < len(boxTypes):
            num_boxes, units_per_box = boxTypes[i]
            boxes_to_consume = min(truckSize, num_boxes)
            truckSize -= boxes_to_consume
            res += boxes_to_consume * units_per_box
            i += 1
        return res