class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = len(arr)-1
        while left<right:
            middle = (left +right) //2
            if arr[middle]>arr[middle-1] and arr[middle]>arr[middle+1] :
                return middle
            if(arr[middle]>arr[middle-1]):
                left = middle + 1
            else:
                right = middle
        return left
    
sol = Solution()
arr1=[0,1,0]
arr2=[0,1,2,0]
arr3=[24,69,100,99,79,78,67,36,26,19]
index_result1=sol.peakIndexInMountainArray(arr1)
index_result2=sol.peakIndexInMountainArray(arr2)
index_result3=sol.peakIndexInMountainArray(arr3)

print(f"arr: {arr1}, \t' result: {index_result1} " )
print(f"arr: {arr2}, \t' result: {index_result2} " )
print(f"arr: {arr3}, \t' result: {index_result3} " )