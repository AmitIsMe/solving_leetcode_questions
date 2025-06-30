import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output =[]             # will store maximum VALUES
        q= collections.deque() # will store INDEXES of List elements (not actual values)
        
        l=r=0 # Left and right pointers to define the current sliding window
        
        # Iterate over the array length, using the RIGHT pointer
        while r<len(nums):
            # in order to maintain a DECREASING order deque
            # Remove elements from the deque's RIGHT end (q[-1]),
            # if they are smaller than the current element (nums[r])
            while q and nums[q[-1]] < nums[r]:
                q.pop() # remove from the right end 
            
            q.append(r) # Add the current element index to the RIGHT of the deque
            
            # Remove the leftmost index if it's outside the bounds of the sliding window
            if l > q[0]:
                q.popleft()
            
            #  Once we got to the position in which r+1 = k,
            #  for every iteration, we need to take a snapshot of the maximum value
            if r+1 >= k:
                output.append(nums[q[0]]) # The maximum value is at the deque's leftmost index
                l+=1   # Slide the window by moving the left pointer
                
            r += 1 # Expand the window by moving the right pointer
        
        return output

#*-------Tests-------#
sol = Solution()
nums, k = [2,3,-1,-3,-2,3,6,7], 5
test1=sol.maxSlidingWindow(nums,k )
print(f"{test1}")
# nums,k = [1], 1
# test2=sol.maxSlidingWindow(nums,k )
# print(f"{test2}")
#*-------------------#
#^ Time Complexity:
#^      O(n)
#^ Space Complexity: 
#^      O(k)