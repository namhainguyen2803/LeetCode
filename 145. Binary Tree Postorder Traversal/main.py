# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """       
        if root == None:
            return []
        else: 
            frontier_1 = list()
            frontier_2 = list()
            frontier_1.append(root)
            while len(frontier_1) != 0:
                element = frontier_1.pop()
                frontier_2.append(element.val)
                if element.left != None:
                    frontier_1.append(element.left)
                if element.right != None:
                    frontier_1.append(element.right)
            res = list()
            for i in range(1, len(frontier_2)+1):
                res.append(frontier_2[len(frontier_2)-i])
            return res