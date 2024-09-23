from typing import List
from sortedcontainers import SortedDict

class SummaryRanges:
    def __init__(self): 
        self.treeMap = SortedDict() # data struct that keeps the numbers in sorted order.

    def addNum(self, value: int) -> None: #* time O(logn)
        self.treeMap[value] = True

    def getIntervals(self) -> List[List[int]]: #* time O(n)
        res = []
        for key in self.treeMap:
            #~ case 1: consecutive 
            if res and res[-1][1] +1 == key: #! res[-1][1] = end of the last interval in res
                res[-1][1]= key              #! extend the last interval in res
            #~ case 2: Not consecutive 
            else:
                res.append([key,key])       #! create a new interval
        return res

#*-------Tests-------#
obj = SummaryRanges()
print(obj.addNum(1))      # arr = [1]
print(obj.getIntervals()) # return [[1, 1]]
print(obj.addNum(3))      # arr = [1, 3]
print(obj.getIntervals()) # return [[1, 1], [3, 3]]
print(obj.addNum(7))      # arr = [1, 3, 7]
print(obj.getIntervals()) # return [[1, 1], [3, 3], [7, 7]]
print(obj.addNum(2))      # arr = [1, 2, 3, 7]
print(obj.getIntervals()) # return [[1, 3], [7, 7]]
print(obj.addNum(6))      # arr = [1, 2, 3, 6, 7]
print(obj.getIntervals()) # return [[1, 3], [6, 7]]
#*-------------------#
#^ Time Complexity:
#^ O(n)
#^ Space Complexity: 
#^ O(n)