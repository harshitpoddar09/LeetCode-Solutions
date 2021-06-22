class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            if 'R' in board[i]:
                rook=board[i].index('R')
                break
        ans=0
        for a in range(rook+1,8):
            if board[i][a]=='B':
                break
            elif board[i][a]=='p':
                ans+=1
                break
        for b in range(rook-1,-1,-1):
            if board[i][b]=='B':
                break
            elif board[i][b]=='p':
                ans+=1
                break
        for c in range(i+1,8):
            if board[c][rook]=='B':
                break
            elif board[c][rook]=='p':
                ans+=1
                break
        for d in range(i-1,-1,-1):
            if board[d][rook]=='B':
                break
            elif board[d][rook]=='p':
                ans+=1
                break
        return ans