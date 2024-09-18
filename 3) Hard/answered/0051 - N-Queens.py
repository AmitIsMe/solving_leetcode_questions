
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        col_set = set()
        pos_diag_set = set() # (row+col)
        neg_diag_set= set() # (row-col)
        res=[]
        # initialize empty board 
        board=[["."]*n for row in range(n)] 
        
        def backtrack(r):
            if r == n: #~ Base case
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col_set or (r+c) in pos_diag_set or (r-c) in neg_diag_set:
                    continue
                
                col_set.add(c)
                pos_diag_set.add(r+c)
                neg_diag_set.add(r-c)
                board[r][c] = "Q"
                
                backtrack(r+1)
                
                col_set.remove(c)
                pos_diag_set.remove(r+c)
                neg_diag_set.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res

#*-------Tests-------#
sol = Solution()
test1=sol.solveNQueens(4)
print(f"{test1}")
#*-------------------#
#^ Time Complexity:
#^  O(n!)
#^ Space Complexity: 
#^ O(n⋅n!)