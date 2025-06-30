
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        col_set = set()      # (↕)
        neg_diag_set= set()  # Tracks the diagonal where (row - col) is constant (↘)
        pos_diag_set = set() # Tracks the diagonal where (row + col) is constant (↗)
        
        res=[]
        # Initialize an empty chess board, where "." represents an empty cell
        board=[["."]*n for row in range(n)] 
        
        # Helper function: to perform backtracking and explore all possible queen placements row by row
        def backtrack(r):
            # Exit case: If we've placed queens on all rows, it's a valid solution
            if r == n: #~  case
                # Convert the board into a list of strings and add to result
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # Iterate through each column in the current row
            for c in range(n):
                # if there's a queen in the same column or diagonal, Skip current column
                if c in col_set or (r+c) in pos_diag_set or (r-c) in neg_diag_set:
                    continue
                
                # Place a queen on the board at position (r, c)
                col_set.add(c)
                pos_diag_set.add(r+c)
                neg_diag_set.add(r-c)
                board[r][c] = "Q"
                
                # Move to the next row and continue placing queens
                backtrack(r+1)
                
                # Backtrack: Remove the queen and explore other possibilities
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
#^      worst case: O(n!)
#^ Space Complexity: 
#^      Board: O(n²), Call Stack and Sets: O(n) = total:O(n²)