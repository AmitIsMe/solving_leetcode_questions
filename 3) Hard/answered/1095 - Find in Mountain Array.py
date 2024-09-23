# class MountainArray:
#     def get(self, index: int) -> int:
#     def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        # pre-mission = find the peak 
        l, r = 1,length -2 # pointers
        while l<=r:
            m= (l+r) // 2
            left = mountain_arr.get(m-1)  # values
            mid = mountain_arr.get(m)     # values
            right = mountain_arr.get(m+1) # values
            if left < mid < right:
                l = m+1
            elif left > mid > right:
                r = m-1
            else:
                break
        peak = m
        
        # search left portion
        l, r = 0, peak
        while l <= r:
            m = (l+r)//2
            val = mountain_arr.get(m)
            if val < target:
                l = m+1
            elif val > target:
                r = m-1
            else:
                return m
        # search right portion
        l, r = peak, length -1 
        while l <= r:
            m = (l+r)//2
            val = mountain_arr.get(m)
            if val > target:
                l = m+1
            elif val < target:
                r = m-1
            else:
                return m
            
        return -1


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