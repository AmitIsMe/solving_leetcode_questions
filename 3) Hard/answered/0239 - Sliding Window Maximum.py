import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output =[]
        q= collections.deque() # will store array indexes
        l=r=0
        while r<len(nums):
            #pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # remove left value from the window
            if l>q[0]:
                q.popleft()
            
            if r+1 >= k:
                output.append(nums[q[0]])
                l+=1
            r += 1
        return output

#*-------Tests-------#
sol = Solution()
nums, k = [1,3,-1,-3,5,3,6,7], 3
test1=sol.maxSlidingWindow(nums,k )
print(f"{test1}")
nums,k = [1], 1
test2=sol.maxSlidingWindow(nums,k )
print(f"{test2}")
#*-------------------#
#^ Time Complexity:
#^ 
#^ Space Complexity: 
#^ 