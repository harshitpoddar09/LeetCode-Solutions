class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0]*(n+1)
        for i,j,k in bookings:
            ans[i-1]+=k
            ans[j]-=k
        for s in range(1,len(ans)):
            ans[s]+=ans[s-1]
        return ans[:-1]