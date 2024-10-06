class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        r_wall =l_wall = 0
        max_right=[0]*(n) # helper array
        max_left = [0]*(n)# helper array
        
        for i in range(n):
            j= -i-1 # as i go forward, j go backwards
            max_left[i]=l_wall
            max_right[j]=r_wall
            l_wall=max(l_wall,height[i])
            r_wall=max(r_wall,height[j])
        sum_trap_water=0
        for i in range(n):
            pot = min(max_left[i],max_right[i])
            sum_trap_water+=max(0,pot-height[i])
        return sum_trap_water
    
#*-------Tests-------#
sol = Solution()
array1 = [0,1,0,2,1,0,1,3,2,1,2,1]
test1=sol.trap(array1 )
print(f"array1: {array1}: {test1}")
#*-------------------#
#^ Time Complexity:
#^ Sum of 2 iterations on the array size which is:O(2n) ~ O(n).
#^ Space Complexity:  
#^ I created 2 additional arrays in the size of n for both of them which is O(2n)~ O(n)