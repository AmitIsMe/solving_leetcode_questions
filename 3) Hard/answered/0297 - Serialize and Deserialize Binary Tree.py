# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # input: root node of a tree
    # output: array of STRINGS that will be join with a ", " between the numbers in to a single string
    def serialize(self, root):
        res =[]
        
        def preOrderDfs(node):
            if not node:        #base case: node is null
                res.append("N") # represent null node
                return
            
            # current nude is not null
            res.append(str(node.val)) # convert the number to a string
            preOrderDfs(node.left)       # because we do preOrder dfs, continue down the left subtree recursively 
            preOrderDfs(node.right)
        
        preOrderDfs(root)        # start the preOrder process 
        return ", ".join(res) # returns the array as a single string
    
    # input:  array of STRINGS, joined with a ", " between the numbers in to a single string
    # output: root node of a tree
    def deserialize(self, data):
        values = data.split(", ") # split the single string, to array of values
        
        self.i = 0 # class scope variable, controls iterations in the recursion process from the first index
        
        def preOrderDfs(): # no need to pass variable because its use the class variable
            #if the array of values, at the global index
            if values[self.i] == "N": # our agreed null flag
                self.i +=1            # even though the value is null, keep moving on the values array
                return None
            
            node = TreeNode(int(values[self.i])) # convert the string value to an int treenode
            self.i += 1                # move position on the values array, after we have the parent node
            node.left  = preOrderDfs() # because we do preOrder dfs, continue down the left subtree recursively 
            node.right = preOrderDfs()
            return node
        
        return preOrderDfs() # start the preOrder process 

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