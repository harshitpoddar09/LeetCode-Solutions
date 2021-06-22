class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        n=1
        stack=[]
        while stack!=target:
            stack.append(n)
            ans.append('Push')
            if n not in target:
                ans.append('Pop')
                stack.pop()
            n+=1
        return ans