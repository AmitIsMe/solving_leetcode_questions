from typing import List
from sortedcontainers import SortedDict

class SummaryRanges:
    def __init__(self): 
        # SortedDict = data structure that automatically keeps its keys in sorted order.
        # We'll use this to store the encountered numbers, ensuring that we can iterate over them in ascending order.
        self.treeMap = SortedDict() 

    def addNum(self, value: int) -> None:
        self.treeMap[value] = True # indicates that we have a encountered this number, 
        #we only care about the treeMap's keys (the numbers themselves).

    #rebuild treeMap's keys to list of disjoint intervals from scratch every time it is called.
    def getIntervals(self) -> List[List[int]]:
        intervals = []  # To store the result list of disjoint intervals
        
        # Iterate over each key (number) in treeMap.
        for key in self.treeMap: #choose all the intervals, and get the end of the interval value 
            
            # If 'intervals' is not empty and the current key is consecutive to the last interval's end,
            # we can extend the last interval to include this key.
            if intervals and intervals[-1][1] + 1 == key:
                intervals[-1][1] = key # Extend the last interval to include the current key
            else:
                # If the current key is not consecutive with the last interval, start a new interval.
                # The new interval will have 'key' as both the start and the end (a single number interval).
                intervals.append([key, key])
        
        return intervals

#*-------Tests-------#
obj = SummaryRanges()
obj.addNum(2)      
print(obj.getIntervals()) 
obj.addNum(3)      
print(obj.getIntervals())
obj.addNum(1)      
print(obj.getIntervals())
obj.addNum(2)      
print(obj.getIntervals())
obj.addNum(6)      
print(obj.getIntervals())
#*-------------------#
#^ Time Complexity:
#^ O(n)
#^ Space Complexity: 
#^ O(n)