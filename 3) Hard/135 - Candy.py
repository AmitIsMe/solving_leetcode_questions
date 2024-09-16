class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # create a "Dummy array" in which every kid get at least one candy
        candies= [1] * len(ratings)
        # 1) Left -> Right
        for i in range(1,len(ratings)):
            if ratings[i-1]<ratings[i]:
                candies[i]= candies[i-1]+1
                
        # 2) Right -> Left
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candies[i]=max(candies[i],candies[i+1]+1)
        #     print(candies[i], end=", ")
        # print()
        return sum(candies)

#*-------Tests-------#
sol = Solution()
array1 = [1,0,2]
# array2 = [1,2,2]
array2 = [2,3,4,5]
array3=[1,3,2,2,1]
array4=[1,2,87,87,87,2,1]
test1=sol.candy(array1 )
print(f"array1: {array1}: {test1}")
test2=sol.candy(array2)
print(f"array2: {array2}: {test2}")
test3=sol.candy(array3)
print(f"array3: {array3}: {test3}")
test4=sol.candy(array4)
print(f"array4: {array4}: {test4}")

#^ Time Complexity:
#^ O(n), where n is the number of children, since we make two linear passes over the array. 
#^ Space Complexity: 
#^ O(n) due to the extra candies array.