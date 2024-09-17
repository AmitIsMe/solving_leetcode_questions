class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        iteration=1
        
        s_len, p_len = len(s), len(p)
        matrix = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        #~ Base case: An empty string matches an empty pattern
        matrix[0][0] = True
        
        #~ Pattern case 1: pattern contains '*' 
        # 1.1) till when pattern can be equal to an empty string.
        # 1.2) '*' MUST have a preceding english char or a '.'
        for j in range(2, p_len + 1):
            if p[j - 1] == '*':
                # Propagate True/False if pattern up till now, could be an empty string
                matrix[0][j] = matrix[0][j - 2]

        for row in range(1, s_len + 1):     # Iterate over - s.char's = rows
            print(f"iteration:{iteration}")
            for col in range(1, p_len + 1):  # Iterate over - pattern char's = columns
                
                #~ Case 2: current p.char is NOT '*' => compare CURRENT CHAR's
                #? 2.1 current p.char == current s.char
                #? 2.2 current p.char == accept any char wildCard
                if p[col - 1] == s[row - 1] or p[col - 1] == '.':
                    #* current cell = propagate the "base case" previous state
                    matrix[row][col] = matrix[row - 1][col - 1]
                
                #~ Case 3: current p.char IS '*'  => compare PRECEDING char's
                elif p[col - 1] == '*':
                    #* 3.1)  if preceding char accrues !ZERO! times
                    #! propagate from same line, before the char and the '*'. (2 columns!)
                    matrix[row][col] = matrix[row][col - 2]

                    # ~3.2) check if: preceding char accrues !one or more! times
                    #? OR preceding p.char = !current! s.char
                    #? OR preceding p.char = accept any char wildCard
                    if p[col - 2] == s[row - 1] or p[col - 2] == '.':
                        matrix[row][col] = matrix[row][col] or matrix[row - 1][col]
            # Print each row in the matrix
            iteration+=1
            for row in matrix:
                print(row)
            print(f"")
        # The answer is in last cell of the matrix
        return matrix[s_len][p_len]

#*-------Tests-------#
sol = Solution()
s = "bbbc"
p = "bb.*c*"
print(f"p: {p}, s: {s}")
test1=sol.isMatch(s,p )
print(f"p: {p}, s: {s}, test1: {test1}")
#*-------------------#
#^ Time Complexity:
#^ O(n * m)
#^ Space Complexity: 
#^ O(n * m)