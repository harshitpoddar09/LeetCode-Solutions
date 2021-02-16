#Submission 1
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i!=j:
                    if arr[i]==2*arr[j]:
                        return 'true'
        else:
            print('false')

#Submission 2 (faster)
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if 0 in arr:
            arr.remove(0)
        for i in arr:
            if 2*i in arr:
                return 1
        return 0
