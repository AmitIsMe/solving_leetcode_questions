class Solution:
    def countOrders(self, n: int) -> int:
        # n = number of orders
        # valid pair = (Pi,Di)
        # x * (x-1) = choices 
        # x * (x-1) / 2  = VALID choices 
        slots = 2*n # number of slots to fill (fetch and deliver)
        res = 1
        while slots > 0:
            validChoices = slots * (slots -1) // 2 # probability formula for this type of question
            res *= validChoices
            slots -=2
        return res % (10**9 +7) # question requirement

#*-------Tests-------#
sol = Solution()
test1=sol.countOrders(3)
print(f"{test1}")

#*-------------------#
#^ Time Complexity:
#^ O(n)
#^ Space Complexity: 
#^ O(1)