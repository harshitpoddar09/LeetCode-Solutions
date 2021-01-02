class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target)
        letters.sort()
        for i in range(len(letters)):
            if letters[i]==target:
                target_index=i
        if target_index==len(letters)-1:
            ans=letters[0]
        else:
            ans=letters[target_index+1]
        return ans