import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root != None:
            frontier = collections.deque()
            frontier.append([root, 1])
            max_depth = 0
            while len(frontier) != 0:
                element = frontier.popleft()
                
                if max_depth < element[1]:
                    max_depth = element[1]
                
                if element[0].left != None:
                    frontier.append([element[0].left, element[1]+1])
                if element[0].right != None:
                    frontier.append([element[0].right, element[1]+1])
            return max_depth
        else:
            return 0

if __name__ == "__main__":
    sol = Solution()
    
    lis = [3,9,20,None,None,15,7]
    
    p3 = TreeNode(3)
    p9 = TreeNode(9)
    p20 = TreeNode(20)
    p15 = TreeNode(15)
    p7 = TreeNode(7)
    p3.left = p9
    p3.right = p20
    p20.left = p15
    p20.right = p7
    
    print(sol.maxDepth(p3))