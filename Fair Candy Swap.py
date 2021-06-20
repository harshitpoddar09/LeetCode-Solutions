#Submission 2 - 348ms
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff=(sum(A)-sum(B))//2
        A=set(A)
        B=set(B)
        for i in A:
            if (i-diff) in B:
                return [i,i-diff]

#Submission 1 - 3064ms
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a_sum=sum(A)
        b_sum=sum(B)
        if a_sum>b_sum:
            for i in A:
                if (i-(a_sum-b_sum)//2) in B:
                    return [i,i-(a_sum-b_sum)//2]
        else:
            for i in B:
                if (i-(b_sum-a_sum)//2) in A:
                    return [i-(b_sum-a_sum)//2,i]