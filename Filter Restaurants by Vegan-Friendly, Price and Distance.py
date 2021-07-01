#Submission 1 - 372ms (faster than 9%)
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        good=[]
        if veganFriendly==1:
            for i in restaurants:
                if i[2]==1 and i[3]<=maxPrice and i[4]<=maxDistance:
                    good.append(i)
        else:
            for i in restaurants:
                if i[3]<=maxPrice and i[4]<=maxDistance:
                    good.append(i)
        good=sorted(good,key=lambda x:x[0],reverse=True)
        good=sorted(good,key=lambda y:y[1],reverse=True)
        return [j[0] for j in good]

#Submission 2 - 360ms (faster than 15%)
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        good=[]
        for i in restaurants:
            if veganFriendly==1:
                if i[2]==1 and i[3]<=maxPrice and i[4]<=maxDistance:
                    good.append(i)
            else:
                if i[3]<=maxPrice and i[4]<=maxDistance:
                    good.append(i)
        good=sorted(good,key=lambda x:x[0],reverse=True)
        good=sorted(good,key=lambda y:y[1],reverse=True)
        return [j[0] for j in good]