"""
so we could form a tree first or do this iteratively
"""

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        direct_mapping = {}
        for emp in employees:
            direct_mapping[emp.id] = emp
        queue = [direct_mapping[id]]
        ids = set()
        while len(queue):
            emp_to_process = queue.pop(0)
            ids.add(emp_to_process.id)
            for s_id in emp_to_process.subordinates:
                queue.append(direct_mapping[s_id])
        return sum([direct_mapping[id].importance for id in ids])