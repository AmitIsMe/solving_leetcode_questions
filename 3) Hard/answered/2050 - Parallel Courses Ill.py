from typing import List
from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        max_time = {} # cashing mechanism,  map the time of each course {src:max_time}
        
        adj = defaultdict(list) # convert 2d array to adjacent courses hashmap
        for src, dst in relations: # create the edges =  src->dst
            adj[src].append(dst)
        
        def dfs(src):
            # utilizing the cashing mechanism => fetch course max_time 
            if src in max_time:#~Edge case: already visited
                return max_time[src]
            # if we have'nt cash the time to the src, compute it
            res = time[src-1] #! time is zero indexed while src is indexed from 1
            
            # Recursively calculate the maximum time for all dependent courses
            for neigh in adj[src]:
                # Choose the maximum time between current course time and the time including the dependent courses
                res = max(res, time[src-1]+dfs(neigh))
                
            # Store the calculated maximum time for the current course in the cache
            max_time[src] = res
            return res
        
        #main dfs call
        # Call DFS for each course to ensure all courses are processed
        # Note: course indices start from 1 to n (inclusive)
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
#^      O(n+E)
#^ Space Complexity: 
#^      O(n+E)