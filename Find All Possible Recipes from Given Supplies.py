class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies=set(supplies)
        ans=[]
        idx=[i for i in range(len(recipes))]
        while idx:
            a=len(idx)
            for i in idx:
                new=[]
                flag=1
                for j in ingredients[i]:
                    if j not in supplies:
                        flag=0
                        break
                if flag:
                    ans.append(recipes[i])
                    supplies.add(recipes[i])
                    idx.remove(i)
            if len(idx)==a:
                break        
        return ans