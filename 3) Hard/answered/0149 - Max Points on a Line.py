import collections
class Solution(object):
    def maxPoints(self, points):
        if len(points) < 2: #~ edge case 
            return len(points)
        
        # helper function - reduce the slope fraction, to its simplest form.
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        res = 0 # track the maximum number of points that lie on the same line.

        # Iterate through each point, treating it as the starting point (p1) for slope calculation.
        for i in range(len(points)):
            p1 = points[i]
            # Dictionary to count the number of points that share the same slope with respect to p1.
            count = collections.defaultdict(int)
            duplicate = 0
            current_max = 0
            
            # Compare p1 with every other point (p2) after it.
            for j in range(i+1,len(points)):
                p2 = points[j]
                
                # Calculate the difference in y and x coordinates (dy, dx) between p1 and p2.
                dy = p2[1]-p1[1] 
                dx = p2[0]-p1[0]
                
                if dx == 0 and dy == 0:
                    duplicate += 1
                    continue
                
                # Reduce the slope (dy/dx) to its simplest form using the GCD.
                g = gcd(dx, dy)
                # Store slope as a tuple (dy, dx) for integer accuracy.
                slope = (dy // g, dx // g) #  without risking the rounding errors that can happen with floating-point division
                # Increment the count for this slope. Points sharing the same slope are collinear.
                count[slope]+=1 #! we found another point, increment the max
                # Update the maximum number of points that share the same slope with p1.
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