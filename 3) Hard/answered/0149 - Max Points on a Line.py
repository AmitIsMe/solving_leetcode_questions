import collections
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #~ edge case 
        if len(points) < 2:
            return len(points)
        # helper function
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        res = 0
        
        for i in range(len(points)):
            p1 = points[i]
            count = collections.defaultdict(int)
            duplicate = 0
            current_max = 0
            
            for j in range(i+1,len(points)):
                p2 = points[j]
                
                dy = p2[1]-p1[1] 
                dx = p2[0]-p1[0]
                
                if dx == 0 and dy == 0:
                    duplicate += 1
                    continue
                
                g = gcd(dx, dy)
                slope = (dy // g, dx // g)
                count[slope]+=1 #! we found another point, increment the max
                current_max = max(current_max, count[slope])
                
            res = max(res, current_max + duplicate +1) #! increment last time, to add the compared point to the current slope
                
        return res

#*-------Tests-------#
sol = Solution()
points1 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
test1=sol.maxPoints(points1)
print(f"{test1}")
points2 = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]
test2=sol.maxPoints(points2)
print(f"{test2}")
points3 = [[0,1], [0,0]]
test3=sol.maxPoints(points3)
print(f"{test3}")
#*-------------------#
#^ Time Complexity:
#^ O(n^2)
#^ Space Complexity: 
#^ O(n)