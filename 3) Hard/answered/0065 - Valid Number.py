class Solution:
    def isNumber(self, s: str) -> bool:
        # Initialize flags to track what has been encountered in the string:
        # digit: indicates if a digit has been encountered
        # dec:   indicates if a decimal point ('.') has been encountered
        # e:     indicates if an exponent ('e' or 'E') has been encountered
        # symbol:indicates if a sign ('+' or '-') has been encountered
        digit,dec,e,symbol = False,False,False,False

        for c in s:
            #~ 1) case: c -> digit
            if c in "0123456789":
                digit = True
            
            #~ 2) case: c -> symbol ('+' or '-' sign)
            elif c in "+-":
                # A sign is only allowed at the beginning or immediately after an exponent
                if symbol or digit or dec:
                    return False # Invalid if sign appears after digit or decimal point
                else:
                    symbol=True #* a valid place for a symbol
            
            #~ 3) case: c -> exponent
            elif c in "Ee":
                # Exponent is valid only if there was a number before it, and the exponent cannot appear twice in arrow 
                if not digit or e:
                    return False #! valid number could not start with exponent (without base number), or 2 'e' in a row
                else:
                    e=True        #* valid use of an exponent
                    symbol= False # 1. we allow to accept optional symbol after exponent
                    dec = False   # 2. No decimals allowed after an exponent
                    digit = False # 3. we Must get at least 1 digit after the exponent, in order to build a valid number
            #~ 4) case: c -> Decimal
            elif c=='.':
                # '.' cannot appear twice in arrow, '.' could not a appear after 'e'
                if dec or e:
                    return False 
                else:
                    dec = True #* valid place to put the decimal point 
            
            #~ 5) case: c -> invalid character
            else:
                return False
        
        return digit
#*-------Tests-------#
sol = Solution()

strings = ["abc", "1a","95a54e53","-0.1", "+3.14", "-123.456e789","1e","e3","--6", "-+3"]
for str in strings:
    test1=sol.isNumber(str)
    print(f"str:{str} |\t {test1}")

#* valid numbers: 
#* legal int: "2", "0089", "2e10", "-90E3", "3e+7", "+6e-1", 
#* legal double: "4." , "-.9","53.5e93", 
#* sign numbers: "-0.1", "+3.14", "-123.456e789"

#* whitelist: E,e,e+,e-,'.'
#*      1) (+/-) (num).num
#*      2) legal exponent = num*e(+/-)num

#! not valid numbers:  
#! blackList: 
#!      1.letter that isn't e (after lowering the srt):
#!                  cases: "abc", "1a","95a54e53"
#!      2.'e' without a digit before
#!                  cases: "1e",
#!      3.'e' without a proceeding digit after e
#!                  cases: "e3",
#!      4. a decimal exponent is INVALID 'e'
#!                  cases: "99e2.5", 
#!      5.two symbol(+/-) one after the other
#!                  cases: "--6", "-+3", 

#*-------------------#
#^ Time Complexity:
#^      O(n)
#^ Space Complexity: 
#^      O(1)