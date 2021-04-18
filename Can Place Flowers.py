class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        while i<len(flowerbed)-1:
            if flowerbed[i]==0 and flowerbed[i+1]==0:
                n-=1
                flowerbed[i]=1
                i+=2
            elif flowerbed[i]==1:
                i+=2
            else:
                i+=1
        if len(flowerbed)>=3:
            if flowerbed[-1]==0 and flowerbed[-2]==0 and flowerbed[-3]==1:
                n-=1
        if len(flowerbed)==1 and flowerbed[0]==0:
            n-=1
        return n<=0