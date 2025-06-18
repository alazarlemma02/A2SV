# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

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
        emp_map = defaultdict(int)

        for emp in employees:
            emp_map[emp.id] = emp
        
        def dfs(id):
            total_imp = emp_map[id].importance

            for sub in emp_map[id].subordinates:
                total_imp += dfs(sub)

            return total_imp
        
        return dfs(id)



