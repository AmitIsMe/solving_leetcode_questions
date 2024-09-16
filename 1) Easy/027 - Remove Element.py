class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums);
        i=0;
        while (i < len(nums)):
            if nums[i]==val:
                k-=1;
                nums.pop(i);
                nums.append("_");
                continue
            i+=1;

        return k

#*-------Tests-------#
sol = Solution()
nums = [3,2,2,3]; val = 3;
print(f"Question: nums: {nums}, val: {val}")
k=sol.removeElement(nums,val)
print(f"Result: nums: {nums}, k: {k}")

#^ Time Complexity:
#^ O(n)
#^ Space Complexity: 
#^ O(n)