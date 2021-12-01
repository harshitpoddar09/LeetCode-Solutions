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
        d={}
        for emp in employees:
            d[emp.id]=[emp.importance,emp.subordinates]
        ans=0
        stack=[id]
        while stack:
            for j in d[stack[0]][1]:
                stack.append(j)
            ans+=d[stack[0]][0]
            stack.pop(0)
        return ans