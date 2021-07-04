class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed)<len(name):
            return False
        i=0
        j=0
        while i<len(name):
            key=name[i]
            sim_name=1
            while i<len(name)-1 and name[i]==name[i+1]:
                sim_name+=1
                i+=1
            sim_typed=1
            if j>=len(typed) or typed[j]!=key:
                return False
            while j<len(typed)-1 and typed[j]==typed[j+1]:
                sim_typed+=1
                j+=1
            if sim_name>sim_typed:
                return False
            i+=1
            j+=1
        if i==len(name) and j==len(typed):
            return True
        else:
            return False