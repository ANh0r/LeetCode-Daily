"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], idx: int) -> int:
        mp = {employee.id: employee for employee in employees}

        def dfs(idx: int) -> int:
            employee = mp[idx]
            total = employee.importance + sum(dfs(subIdx) for subIdx in employee.subordinates)
            return total

        return dfs(idx)