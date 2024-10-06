class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return "" #~ Edge case
        countT,window = {},{}
        
        for letterKey in t:              #* t = requested chars
            countT[letterKey]= 1 + countT.get(letterKey,0)
        
        have, need = 0,len(countT)
        res,resLen = [-1,-1], float("inf")
        left = 0
        for right in range(len(s)): #*
            letter = s[right]
            window[letter] = 1 + window.get(letter,0)
            
            if letter in countT and window[letter] == countT[letter]:
                have +=1
            
            while have == need:
                #! update our result
                if (right-left +1)<resLen:
                    res = [left,right]
                    resLen = (right-left+1)
                #! pop from the left of our window
                window[s[left]]-=1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -=1
                left+=1
        left,right = res
        return s[left:right+1] if resLen != float("inf") else ""


#*-------Tests-------#
sol = Solution()
array1 = ["ADOBECODEBANC","ABC"]
test1=sol.minWindow(array1[0],array1[1] )
print(f"{test1}")
#*-------------------#
#^ Time Complexity:
#^ 
#^ Space Complexity: 
#^ 