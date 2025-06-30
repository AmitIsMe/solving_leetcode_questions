# class MountainArray:
#     def get(self, index: int) -> int:
#     def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        # first mission: Find the peak element in the mountain array using binary search
        # The peak element is the maximum value, and it cannot be at index 0 or length-1.
        l= 1
        r =length -2 
        
        while l<=r: # first bin search (to find the peak)
            m = (l+r) // 2
            left = mountain_arr.get(m-1) # values
            mid  = mountain_arr.get(m)   # values
            right= mountain_arr.get(m+1) # values
            if left < mid < right:   # ascending = the peak is to the right = push forward left pointer 
                l = m+1
            elif left > mid > right: # descending = the peak is to the left = pull back    right pointer
                r = m-1
            else:
                break # the only left situation is left < mid > right
        peak = m # we reached the peak 
        
        # second mission: find the minimum index that the target value can be located at, 
        # we will start looking for it in the left portion of the mountain (Ascending section)
        l=0 
        r=peak
        # if the target value is NOT in the Ascending section,
        while l <= r: # this condition will break before we get into the else statement
            m = (l+r)//2
            value = mountain_arr.get(m) # get value at the 'm' index
            if value < target: #if the value at the index 'm' is less then the target
                l = m+1        # look for the target after the 'm' index
            elif value > target: #if the value at the index 'm' is BIGGER then the target
                r = m-1          # look for the target BEFORE the 'm' index
            else: # only condition we will get here is if target = value
                return m
            
        # search right portion (descending section)
        l = peak
        r = length -1   
        while l <= r:
            m = (l+r)//2
            value = mountain_arr.get(m)
            if value > target:
                l = m+1
            elif value < target:
                r = m-1
            else:
                return m
        return -1 # we will get here only if the target never found


# #-------Tests-------#
# sol = Solution()
# array1, target1 = [1,2,3,4,5,3,1], 3
# array2, target2 = [0,1,2,4,2,1], 3

# test1=sol.findInMountainArray(target1,array1)
# print(f"{test1}")
# test2=sol.findInMountainArray(target2,array2)
# print(f"{test2}")
# #-------------------#
#^ Time Complexity:
#^ O(3logn)≈O(logn)
#^ Space Complexity: 
#^ O(1).