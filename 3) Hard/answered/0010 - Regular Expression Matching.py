class Solution(object):
    def isMatch(self, s, p):
        iteration=1 # For debugging purposes: track iterations
        
        s_len, p_len = len(s), len(p)
        
        # Initialize a dynamic prog matrix, where dp[i][j] is True if s[0:i] matches p[0:j]
        # We add 1 extra index, to represents an empty pattern and string.
        matrix = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        
        #~ Base case: An empty string matches an empty pattern
        matrix[0][0] = True
        
        #~ Handle patterns with '*' upon matrix initiation:
        # '*' can only follow a valid character (this is why range can start from 2)
        # the letter that precedes the '*', can a cur "zero or more" of valid character
        for j in range(2, p_len + 1):
            if p[j - 1] == '*':
                # If the pattern char that precedes the '*', a curs zero times => we can be "skip" 2 char "_*"
                # inherit the match state from 2 columns before
                # Matrix movement: Left two columns (← ←)
                matrix[0][j] = matrix[0][j - 2]

        for row in range(1, s_len + 1):      # Iterate over - s.char's = rows
            
            print(f"iteration:{iteration}")  #? for debug only
            
            for col in range(1, p_len + 1):  # Iterate over - p.char's = columns
                
                #~ Case 1: Direct match or wildcard '.'
                # current p.char == current s.char 
                #             OR
                # current p.char == wildcard '.'
                if p[col - 1] == s[row - 1] or p[col - 1] == '.':
                    # current cell = propagate the "base case" state from previous iteration
                    # Matrix movement: Diagonal up-left (↖)
                    matrix[row][col] = matrix[row - 1][col - 1]
                
                #~ Case 2: Pattern contains '*'
                elif p[col - 1] == '*':
                    # 2.1: Treat '*' as zero occurrences of the preceding character
                    # try to check, if we ignore the last two p.chars (the char before '*' and the '*') we have a match
                    # Matrix movement: Left two columns (← ←)
                    matrix[row][col] = matrix[row][col - 2]

                    # 2.2: 
                    # the '*' preceding p.char = current s.char,
                    #                 OR
                    # the '*' preceding p.char = wildcard '.',
                    # Matrix movement: Upwards (↑)
                    if p[col - 2] == s[row - 1] or p[col - 2] == '.':
                        matrix[row][col] = matrix[row][col] or matrix[row - 1][col]
            # Print each row in the matrix
            iteration+=1        #? for debug only
            for r in matrix:    #? for debug only
                print(r)        #? for debug only
            print(f"")          #? for debug only
            
        #* The answer is in last cell of the matrix
        return matrix[s_len][p_len]

#*-------Tests-------#
sol = Solution()
s = "aab"
p = "c*a*b"
# s = "bbbc"
# p = "bb.*c*"
print(f"p: {p}, s: {s}")
test1=sol.isMatch(s,p )
print(f"p: {p}, s: {s}, test1: {test1}")
#*-------------------#
#^ Time Complexity:
#^ O(n * m)
#^ Space Complexity: 
#^ O(n * m)