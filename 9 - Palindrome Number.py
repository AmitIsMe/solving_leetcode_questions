class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        # Store the original number
        original = x
        reversed_num = 0
        
        while( x > 0):
            unit_digit = x%10 #
            reversed_num = reversed_num *10+unit_digit
            x//=10
            print(f"x: {x},reversed_num: {reversed_num}")
            
            
        # Check if the original number is equal to the reversed number
        return original == reversed_num


#*-------Tests-------#
sol = Solution()
test1=sol.isPalindrome(121) # Output: True
test2=sol.isPalindrome(-121)# Output: False
test3=sol.isPalindrome(10)   # Output: False
test4=sol.isPalindrome(4984)  # Output: False

print(f"Test1:{test1}")
print(f"Test2:{test2}")
print(f"Test3:{test3}")
print(f"Test3:{test4}")
