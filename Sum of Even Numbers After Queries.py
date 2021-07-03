class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        a=0
        for i in A:
            if i%2==0:
                a+=i
        for j in queries:
            if A[j[1]]%2==0:
                if j[0]%2==0:
                    a+=j[0]
                else:
                    a-=A[j[1]]
            else:
                if j[0]%2!=0:
                    a+=A[j[1]]
                    a+=j[0]
            A[j[1]]+=j[0]
            ans.append(a)
        return ans