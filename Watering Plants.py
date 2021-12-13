class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        qty=capacity
        ans=0
        for i in range(len(plants)):
            if plants[i]>qty:
                ans+=(2*i)
                qty=capacity
            ans+=1
            qty-=plants[i]
        return ans