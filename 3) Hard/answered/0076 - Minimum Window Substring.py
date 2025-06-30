class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Handle edge case: if t is an empty string, return an empty string
        if t == "": 
            return ""
        
        # Frequency maps: 
        window = {} # tracks the count of characters in the current window of 's'
        countT = {} # holds the count of each character in 't' (target string)
        
        # Populate the frequency map for characters in 't'
        for letter in t:
            countT[letter]= 1 + countT.get(letter,0)
        
        # Variables to track progress:
        have = 0  # Tracks how many unique characters in 't' are satisfied in the current window
        need = len(countT) # The total number of unique characters to match
        
        # Variables to track the minimum window:
        res= [-1,-1] # Stores the indices of the smallest valid window found
        resLen = float("inf") # Tracks the length of the smallest valid window
        left = 0 # The left boundary of the sliding window
        
        # Iterate over 's' with 'right' as the expanding boundary of the window
        for right in range(len(s)):
            letter = s[right]
            # Update the count of the current character in the window
            window[letter] = 1 + window.get(letter,0)
            
            # If the current char, is in 't', and its count in the window matches 'countT'
            if letter in countT and window[letter] == countT[letter]:
                have +=1 # This character's requirement is now satisfied
            
            # as long as we have'nt reached the end of string 's',
            # continue to change leftmost pointer to find if there is more complete appearances ahead
            while have == need:
                # if current window size, is smaller then the global minimum 
                if (right-left +1)<resLen:
                    res = [left,right] # update and store the current windows as the response new minimum. 
                    resLen = (right-left+1)
                
                # Shrink the window from the left by decreasing the count of the leftmost character
                window[s[left]]-=1 
                
                # If the removed character was part of 't' and its count falls below the required amount
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -=1 # The window no longer satisfies this character's requirement
                left+=1 # Move the left pointer to try and find a smaller window
        left,right = res
        # If no valid window is found, return an empty string; otherwise, return the smallest window
        return s[left:right+1] if resLen != float("inf") else ""

#*-------Tests-------#
sol = Solution()
array1 = ["ADOBECODEBANC","ABC"]
test1=sol.minWindow(array1[0],array1[1] )
print(f"{test1}")
#*-------------------#
#^ Time Complexity:
#^      O(m + n)
#^ Space Complexity: 
#^      O(m + n)