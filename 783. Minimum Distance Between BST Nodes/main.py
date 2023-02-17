# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # In-order, using stack
        frontier = list()
        frontier.append(root)
        res = list()
        current = root
        while True:
            if current != None:
                # go to most left node of subtree
                while current.left != None:
                    frontier.append(current.left)
                    current = current.left
            
            # print most left node
            if len(frontier) != 0:
                current = frontier.pop()
                res.append(current.val)
            
            # if the most left node has right subtree, continue that subtree
            if current.right != None:
                current = current.right
                frontier.append(current)
            else:
                current = None
            
            # most right node's properties:
            if len(frontier) == 0 and current == None:
                break


        dp = [0 for i in range(len(res)-1)]
        for i in range(len(dp)):
            dp[i] = abs(res[i+1] - res[i])
        
        return min(dp)
if __name__ == "__main__":
    lis = [27,None,34,None,58,50,None,44]
    sol = Solution()
    p27 = TreeNode(27)
    p34 = TreeNode(34)
    p58 = TreeNode(58)
    p50 = TreeNode(50)
    p44 = TreeNode(44)
    p27.right = p34
    p34.right = p58
    p58.left = p50
    p50.left = p44
    print(sol.minDiffInBST(p27))
    