# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # accepts tree and convert it to an array of STRINGS!
    def serialize(self, root):
        res =[]
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val)) # convert int to string
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ", ".join(res) #returns array
    
    #! accepts array of strings, (after a Tree got converted to array)
    def deserialize(self, data):
        vals = data.split(", ")
        self.i = 0 # global class scope variable to control iteration in the recursion process 
        
        def dfs():
            if vals[self.i] == "N":
                self.i +=1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left =dfs()
            node.right =dfs()
            return node
        return dfs()


#*-------Tests-------#
#! serialize accepts Tree as an inputs
# input = [1,2,3,None,None,4,5]
rootTreeNode = TreeNode(1)                      #       1
rootTreeNode.left = TreeNode(2)                 #      / \
rootTreeNode.right = TreeNode(3)                #     2   3
rootTreeNode.right.left=TreeNode(4)             #        / \
rootTreeNode.right.right=TreeNode(5)            #       4   5

ser = Codec()
deSer = Codec()

# Serialize original tree (tree -> array) 
serialized_data = ser.serialize(rootTreeNode)
print(f"Serialized Original Tree: {serialized_data}")

# Deserialize to get the tree back
deserialized_tree = deSer.deserialize(serialized_data)

# Serialize the deserialized tree again to compare
re_serialized_data = ser.serialize(deserialized_tree)
print(f"Serialized Deserialized Tree: {re_serialized_data}")

# Check if the serialized data before and after is the same
if serialized_data == re_serialized_data:
    print("Deserialization check passed! The trees match.")
else:
    print("Deserialization check failed. The trees do not match.")

#*-------------------#
#^ Time Complexity:
#^ O(n)
#^ Space Complexity: 
#^ O(n)