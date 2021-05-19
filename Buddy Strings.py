class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return 0
        if A==B:
            if len(A)-len(set(A))>0:
                return 1
        swap=[]
        for i in range(len(A)):
            if A[i]!=B[i]:
                swap.append(i)
                if len(swap)>2:
                    return 0
        if len(swap)!=2:
            return 0
        return A[swap[0]]==B[swap[1]] and A[swap[1]]==B[swap[0]]