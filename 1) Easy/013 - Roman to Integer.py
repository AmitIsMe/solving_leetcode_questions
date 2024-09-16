class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Dictionary in constant length, Dictionary lookup = O(1) time complexity
        roman_to_int={
            'I':1,'V':5,'X':10,'L':50,
            'C':100,'D':500,'M':1000
        }

        total = 0
        prev_value=0

        # Loop through each character in the string
        for char in reversed(s):
            current_value = roman_to_int[char]
            # Roman way of subtraction
            if current_value < prev_value:
                total -= current_value
            else: 
                total += current_value

            prev_value = current_value
        return total

#*-------Tests-------#
sol =  Solution()
test1=sol.romanToInt("III")
test2=sol.romanToInt("LVIII")
test3=sol.romanToInt("MCMXCIV")
print(f"Test1: {test1}")
print(f"Test2: {test2}")
print(f"Test3: {test3}")

#^ Time Complexity:
#^ O(n) - Dictionary loop in constant time and one loop in input size 
#^ Space Complexity: 
#^ O(1) - Small dictionary in constant size and few vars