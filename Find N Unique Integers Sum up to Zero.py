class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n%2==0:
            arr=[i for i in range(-n//2,n//2 +1)]
            arr.remove(0)
        else:
            arr=[i for i in range(-n//2 +1,n//2 +1)]
        return arr