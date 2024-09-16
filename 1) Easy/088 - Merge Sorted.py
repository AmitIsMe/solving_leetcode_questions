class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Because we are dealing with 2 non-decreasing order arrays
        # the biggest number in each array should be on the last index
        # accessing the last index is always array size-1
        index_nums1=m-1
        index_nums2=n-1
        #again Because we are writing (accessing)to the last index of the array, we must do (array-size -1)
        index_merge=m+n-1
        # while we didn't finish to iterate over nums2 array, keep scanning it
        
        while index_nums2>=0:
            #? run from the last num1 NON-zero element &  validate that nums1 'index out of bound' 
            # check if we have num1 element to swap
            if index_nums1>=0 and nums1[index_nums1]>nums2[index_nums2]:
                nums1[index_merge]=nums1[index_nums1]
                index_nums1-=1
                
            # nums2 current index has bigger value then nums1 current element
            # we are writing the nums2 current index to the at the current
            else:
                nums1[index_merge]=nums2[index_nums2]
                index_nums2 -=1   
            index_merge -= 1 # after every iteration, we inserted one element from the last index

#*-------Tests-------#
sol = Solution()
nums1=[1,2,3,0,0,0]
m= 3
nums2 = [2,5,6]
n=3
sol.merge(nums1, m, nums2, n)
print(nums1)

#^ Time Complexity:
#^ O(m + n): We iterate through each element of nums1 and nums2 once.
#^ Space Complexity:
#^ O(1): The algorithm uses constant extra space because we modify nums1 in place.