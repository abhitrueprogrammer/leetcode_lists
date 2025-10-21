class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        def findWord_from(row, col, i ):
            if(i == len(word) -1 ):
                return True
            temp = board[row][col]
            board[row][col] = "."
            for dr, dc in d:
                r = row + dr
                c = col + dc 
                if(min(r, c) < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[i+1] ):
                    continue
                if(findWord_from(r, c, i+1)):
                    return True
            board[row][col] = temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == word[0] and findWord_from(i,j,0)):
                    return True
        return False
