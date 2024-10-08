class Solution(object):
    def candy(self, ratings):
        # Initialize an array where each child gets at least one candy initially
        candies= [1] * len(ratings) # helper array
        # First pass: Traverse from left to right
        # Ensure that any child with a higher rating than the one BEFORE, gets more candies than the previous child
        for i in range(1,len(ratings)):
            if ratings[i-1]<ratings[i]:
                candies[i]= candies[i-1]+1
        
        # Second pass: Traverse from right to left
        # Ensure that any child with a higher rating than the NEXT one, also gets more candies than the next child
        
        for i in range(len(ratings)-2,-1,-1): #skip the last index because it has no neighbor
            if ratings[i]>ratings[i+1]:
                # the secrete to this question:
                candies[i]=max(candies[i],candies[i+1]+1)# Use max to keep the higher candy count between the two passes
        return sum(candies)

#*-------Tests-------#
sol = Solution()

#initial=[1,1,1,1,1,1]
array=   [5,4,3,5,6,2]

#L2R    =[1,1,1,2,3,1]
#R2L    =[3,2,1,2,3,1]
test=sol.candy(array )
print(f"array: {array}: {test}")

#^ Time Complexity:
#^      O(n),n = number of children, since we make two linear passes over the array. 
#^ Space Complexity: 
#^      O(n) due to the extra candies array.