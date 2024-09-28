from typing import List
from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        max_time = {} # cashing mechanism,  #src -> max_time
        
        adj = defaultdict(list) # convert 2d array to adjacent courses hashmap
        for src, dst in relations:
            adj[src].append(dst)
        
        def dfs(src):
            # utilizing the cashing mechanism => fetch course max_time 
            if src in max_time:#~Edge case: already visited
                return max_time[src]
            
            res = time[src-1] #! time is zero indexed while src is indexed from 1
            
            for neigh in adj[src]:
                res = max(res, time[src-1]+dfs(neigh))
            max_time[src] = res
            return res
        
        #main dfs call
        for i in range(1,n+1):  #! n courses is indexed from !1! to n
            dfs(i)

        return max(max_time.values())


#*-------Tests-------#
sol = Solution()
n1 = 3
relations1 = [[1,3],[2,3]]
time1 = [3,2,5]
test1=sol.minimumTime(n1,relations1,time1)
print(f"{test1}")

#-------------------#
n2 = 5
relations2 = [[1,5],[2,5],[3,5],[3,4],[4,5]]
time2 = [1,2,3,4,5]
test2=sol.minimumTime(n2,relations2,time2)
print(f"{test2}")
#*-------------------#
#^ Time Complexity:
#^ O(n+e)
#^ Space Complexity: 
#^ 