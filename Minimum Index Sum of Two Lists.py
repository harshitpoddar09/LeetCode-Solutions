#Submission 3 - 180ms
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        ans=[]
        min_val=len(list1)+len(list2)-2
        for i in set(list1).intersection(set(list2)):
            idx=list1.index(i)+list2.index(i)
            if idx<min_val:
                ans=[i]
                min_val=idx
            elif idx==min_val:
                ans.append(i)
        return ans

#Submission 2 - 1100ms
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=[]
        min_val=len(list1)+len(list2)-2
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list2[j]==list1[i]:
                    if i+j<min_val:
                        min_val=i+j
                        ans=[list1[i]]
                    elif i+j==min_val:
                        ans.append(list1[i])
        return ans

#Submission 1 - 960ms
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        min_val=len(list1)+len(list2)-2
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list2[j]==list1[i]:
                    d[list1[i]]=i+j
                    min_val=min(min_val,i+j)
                    break
        ans=[]
        for key,value in d.items():
            if value==min_val:
                ans.append(key)
        return ans