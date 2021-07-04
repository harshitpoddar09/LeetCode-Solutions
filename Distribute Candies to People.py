class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans=[0 for _ in range(num_people)]
        j=1
        i=0
        while candies>=j:
            if i==len(ans):
                i=0
            ans[i]+=j
            candies-=j
            j+=1
            i+=1
        if i==len(ans):
            ans[0]+=candies
        else:
            ans[i]+=candies
        return ans