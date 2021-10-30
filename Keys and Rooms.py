class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack=[0]
        seen=[False]*len(rooms)
        seen[0]=True
        while stack:
            cur=stack.pop()
            for key in rooms[cur]:
                if not seen[key]:
                    stack.append(key)
                    seen[key]=True
        return all(seen)