class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l=0
        r=len(plants)-1
        cura=capacityA
        curb=capacityB
        ans=0
        while l<=r:
            if l!=r:
                if plants[l]>cura:
                    ans+=1
                    cura=capacityA-plants[l]
                else:
                    cura-=plants[l]
                if plants[r]>curb:
                    ans+=1
                    curb=capacityB-plants[r]
                else:
                    curb-=plants[r]
            else:
                if cura>=curb:
                    if plants[l]>cura:
                        ans+=1
                else:
                    if plants[l]>curb:
                        ans+=1
            l+=1
            r-=1
        return ans