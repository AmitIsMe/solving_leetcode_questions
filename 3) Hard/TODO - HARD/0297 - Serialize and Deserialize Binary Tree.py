# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
#*-------Tests-------#
sol = Solution()
root = [1,2,3,None,None,4,5]
test1=sol.serialize(root)
print(f"{test1}")

#*-------------------#
#^ Time Complexity:
#^ 
#^ Space Complexity: 
#^ 