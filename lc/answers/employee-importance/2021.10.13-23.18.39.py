class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {e.id: e for e in employees}
        added = {id}
        total = d[id].importance
        queue = d[id].subordinates
        while len(queue):
            sub_id = queue.pop(0)
            if sub_id not in added:
                added.add(sub_id)
                total += d[sub_id].importance
                queue.extend(d[sub_id].subordinates)
        return total
