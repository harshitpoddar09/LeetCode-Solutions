class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cur=[0]*1001
        for i in trips:
            cur[i[1]]+=i[0]
            cur[i[2]]-=i[0]
        val=0
        for j in cur:
            val+=j
            if val>capacity:
                return False
        return True