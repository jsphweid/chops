"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
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
        adj = {}
        for emp in employees:
            adj[emp.id] = (emp.importance, emp.subordinates)
        def count(emp_id):
            importance, subordinates = adj[emp_id]
            res = importance
            for sub in subordinates:
                res += count(sub)
            return res
        return count(id)