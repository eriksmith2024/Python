
#Please find the given value is availeble in the tree node or not Find in both trees.



class Solution:
   def isSameTree(self, p: TreeNode, q: TreeNode) -> bool: 
  if not p and not q: 
    return True 
  if not p or not q: 
    return False 
  return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# To determine if a given value exists in both binary trees, we can traverse both trees simultaneously and check if the value is found in each of them. Here's how you can achieve this by modifying the given isSameTree function or by creating a new function.

# I'll provide you with a new function that checks for the presence of a value in both trees:



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findInTree(self, root: TreeNode, value: int) -> bool:
        if root is None:
            return False
        if root.val == value:
            return True
        return self.findInTree(root.left, value) or self.findInTree(root.right, value)
    
    def isValueInBothTrees(self, p: TreeNode, q: TreeNode, value: int) -> bool:
        return self.findInTree(p, value) and self.findInTree(q, value)

# Example usage:
# Assuming the trees are defined and the nodes are created:
# tree1 = TreeNode(1)
# tree1.left = TreeNode(2)
# tree1.right = TreeNode(3)
# tree2 = TreeNode(1)
# tree2.left = TreeNode(2)
# tree2.right = TreeNode(3)
# solution = Solution()
# value = 2
# print(solution.isValueInBothTrees(tree1, tree2, value)) # Output: True
