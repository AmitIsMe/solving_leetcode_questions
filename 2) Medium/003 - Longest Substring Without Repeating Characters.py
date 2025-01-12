### acumlate chars

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        l=0
        res=0
        for r in range(len(s)): # INCREASE window = iterator from the right
            while s[r] in charSet:  # LOGICAL GATE = if duplicate letter or not = 
                charSet.remove(s[l]) #removing FIRST Appearance of the repeated char
                l+=1    # DECREASE window = move to next char from the left
            charSet.add(s[r]) # INCREASE window  = add the current char to uniq set
            res = max(res, r-l+1) # check window size
        return res
        

#*-------Tests-------#
sol = Solution()
test1=sol.lengthOfLongestSubstring("abcabcbb")
test2=sol.lengthOfLongestSubstring("bbbbb")
test3=sol.lengthOfLongestSubstring("pwwkew")
print(f"Test: {1},\t :{test1}")
print(f"Test: {2},\t :{test2}")
print(f"Test: {3},\t :{test3}")
#^ Time Complexity:
#^ O(log(num)) - the algorithm processes each digit of input number, and the number of digits grows logarithmically with the input size.
#^ Space Complexity: 
#^ O(log(num)) - the result string grows in proportion to the number of Roman numeral characters, which is logarithmic in terms of the input number.