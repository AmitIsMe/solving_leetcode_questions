from typing import List
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        


#*-------Tests-------#
sol = Solution()
n1 = 6
meetings1 = [[1,2,5],[2,3,8],[1,5,10]]
firstPerson1 = 1
test1=sol.findAllPeople(n1,meetings1,firstPerson1)
print(f"{test1}")
n2 = 6
meetings2 = [[1,2,5],[2,3,8],[1,5,10]]
firstPerson2 = 1
test2=sol.findAllPeople(n2,meetings2,firstPerson2)
print(f"{test2}")

#*-------------------#
#^ Time Complexity:
#^ 
#^ Space Complexity: 
#^ 