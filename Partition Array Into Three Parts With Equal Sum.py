#Submission 2 - 312ms, 20.5mb
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total=sum(arr)
        if total%3!=0:
            return False
        s=0
        count=0
        while arr and count<2:
            s+=arr.pop()
            if s*3==total:
                count+=1
                s=0
        return count==2 and arr and sum(arr)*3==total
        
#Submission 1 - 328ms, 21.2mb
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total=sum(arr)
        if total%3!=0:
            return False
        part1=arr[0]
        i=1
        while part1!=total//3 and i<len(arr)-2:
            part1+=arr[i]
            i+=1
        if part1!=total//3:
            return False
        part2=arr[i]
        i+=1
        while part2!=total//3 and i<len(arr)-1:
            part2+=arr[i]
            i+=1
        if part2!=total//3:
            return False
        part3=arr[i]
        i+=1
        while part3!=total//3 and i<len(arr):
            part3+=arr[i]
            i+=1
        if part3!=total//3:
            return False
        return True          