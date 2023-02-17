# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return 0
        else:
            # Preorder not using stack
            frontier = list()
            frontier.append(root)
            res = list()
            while len(frontier) != 0:
                element = frontier.pop()
                res.append(element.val)
                if element.right != None:
                    frontier.append(element.right)
                if element.left != None:
                    frontier.append(element.left)
            return res
                