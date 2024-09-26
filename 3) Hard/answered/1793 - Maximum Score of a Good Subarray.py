
from typing import List
# You are given an array of integers nums (0-indexed) and an integer k.

# The score of a subarray (i, j) is defined as
#  min(nums[i], nums[i+1], ..., nums[j]) 
# '-'* 
# (j - i + 1).

# A good subarray = subarray where i <= k <= j.

# Return the maximum possible score of a good subarray.

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        left = right = k
        min_val = nums[k]
        max_score =min_val
        
        while(0 < left  or right < n-1):
            if left == 0:
                right+=1
            elif right == n-1:
                left -= 1
            else:
                if nums[left-1] > nums[right+1]:
                    left -= 1
                else:
                    right +=1
            
            # Update the minimum value in the current subarray
            min_val = min(min_val, nums[left], nums[right])
            
            current_score  = min_val * (right-left+1)
            max_score = max(max_score,current_score)
        return max_score


#*-------Tests-------#
sol = Solution()
#                     i, j
#optimal subArray is (1, 5)= len(1, 5)
#
#           [0][1][2][3][4][5]
nums1, k1 = [1, 4, 3, 7, 4, 5], 3
#              [i]    ↑k=3 [j]
#with a score of:      (min=3)   * (5-1+1) = 3 * 5 = 15. 
#                 min(4,3,7,4,5) *  j-i+1                
test1=sol.maximumScore(nums1,k1)
print(f"{test1}")
#todo---------------------------------
#                           i, j
#test2: optimal subarray = (0, 4) 
#
#          [0][1][2][3][4][5][6][7]
nums2,k2 = [5, 5, 4, 5, 4, 1, 1, 1], 0
#      k=0↑[i]         [j]
#
#                min(5,5,4,5,4) *  j-i+1  
#with a score of:    min=4      * (4-0+1) = 4 * 5 = 20.
test2 = sol.maximumScore(nums2,k2)
print(f"{test2}")

#*-------------------#
#^ Time Complexity:
#^ O(n).
#^ Space Complexity: 
#^ O(1).