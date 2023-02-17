class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0]
        def dfs(root):
            if not root:
                return -1
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            res[0] = max(res[0], left+right)
            return max(left, right)
        dfs(root)
        return res[0]

if __name__ == "__main__":
    sol = Solution()
    arr = [4,2,None,1,3]
    p4 = TreeNode(val=4)
    p2 = TreeNode(val=2)
    p1 = TreeNode(val=1)
    p3 = TreeNode(val=3)
    p4.left = p2
    p2.left = p1
    p2.right = p3
    res = sol.diameterOfBinaryTree(p4)
    print(res[0].val, res[1].val)
        