class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # create a mapping  of Roman Numerals to integers
        roman_to_int={
            'I':1,'V':5,'X':10,'L':50,
            'C':100,'D':500,'M':1000
        }

        total = 0
        prev_value=0

        # Loop through each character in the string
        for char in reversed(s):
            current_value = roman_to_int[char]

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