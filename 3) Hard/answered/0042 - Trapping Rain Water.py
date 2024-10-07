class Solution(object):
    def trap(self, height):
        n = len(height)
        r_wall = l_wall = 0
        max_right= [0]*(n) # added array, store the maximum height to the right of each column
        max_left = [0]*(n) # helper array, store the maximum height to the left of each column
        
        # First loop: populate max_left and max_right arrays
        for i in range(n):
            j= -i-1 # as i go forward, j go backwards
            max_left[i] = l_wall # Store the highest wall encountered on the left side up to index i
            max_right[j] = r_wall # Store the highest wall encountered on the right side up to index j (from the end)
            l_wall=max(l_wall,height[i])
            r_wall=max(r_wall,height[j])
        sum_trap_water = 0  # Initialize variable to accumulate the total trapped water
        
        # Second loop: calculate the trapped water
        for i in range(n):
            # The water trapped at index i:
            # is determined by the shorter of the two walls (left and right)
            potential_water = min(max_left[i],max_right[i])
            sum_trap_water += max(0,potential_water - height[i])
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