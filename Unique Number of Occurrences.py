class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence=[]
        for i in set(arr):
            occurence.append(arr.count(i))
        a=sorted(occurence)
        b=sorted(list(set(occurence)))
        return a==b