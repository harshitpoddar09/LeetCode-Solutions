class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack=[start]
        visited=set()
        n=len(arr)
        while stack:
            idx=stack.pop()
            visited.add(idx)
            if arr[idx]==0:
                return True
            i1=idx+arr[idx]
            i2=idx-arr[idx]
            if i1<n and i1 not in visited:
                stack.append(i1)
            if i2>-1 and i2 not in visited:
                stack.append(i2)
        return False