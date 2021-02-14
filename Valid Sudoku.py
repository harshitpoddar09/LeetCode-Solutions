class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans=1
        num=['1','2','3','4','5','6','7','8','9']
        for i in range(9):
            for j in num:
                if board[i].count(j)>1:
                    return 0
        for p in range(9):
            a=[]
            for q in range(9):
                if board[q][p] in num:
                    if board[q][p] not in a:
                        a.append(board[q][p])
                    else:
                        return 0
        for w in range(0,7,3):
            for y in range(0,7,3):
                b=[]
                for x in range(0+w,3+w):
                    for z in range(0+y,3+y):
                        if board[x][z] in num:
                            if board[x][z] not in b:
                                b.append(board[x][z])
                            else:
                                return 0
        return ans