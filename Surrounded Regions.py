class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r=len(board)
        c=len(board[0])
        if r<3 or c<3:
            return board
        def border(i,j):
            if -1<i<r and -1<j<c and board[i][j]=='O':
                board[i][j]='B'
                border(i+1,j)
                border(i-1,j)
                border(i,j+1)
                border(i,j-1)
        for i in range(r):
            border(i,0)
            border(i,c-1)
        for j in range(c):
            border(0,j)
            border(r-1,j)
        for i in range(r):
            for j in range(c):
                cell=board[i][j]
                if cell=='B':
                    board[i][j]='O'
                elif cell=='O':
                    board[i][j]='X'
        return board