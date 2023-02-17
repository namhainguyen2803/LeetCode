

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution(object):
    def diameterOfBinaryTree(self, root: TreeNode):
        frontier = list()
        root.parent = None
        root.visited = False
        frontier.append([root, 0])
        max_dist_from_root = -1
        startpoint = None
        dist_from_root = 0
        while len(frontier) != 0:
            element = frontier.pop()
            print(f"Max dist so far: {max_dist_from_root}, node: {element[0].val}, current dist: {dist_from_root}")
            if max_dist_from_root < dist_from_root:
                max_dist_from_root = dist_from_root
                startpoint = element[0]
            
            if element[0].right != None:
                element[0].right.parent = element[0]
                element[0].right.visited = False
                dist_from_root = element[1] + 1
                frontier.append([element[0].right, dist_from_root])
                
            if element[0].left != None:
                element[0].left.parent = element[0]
                element[0].left.visited = False
                dist_from_root = element[1] + 1
                frontier.append([element[0].left, dist_from_root])
        print("<=====END 1=====>")
        
        
        frontier_2 = list()
        frontier_2.append([startpoint, 0])
        max_dist_from_ptr = -1
        endpoint = None
        dist_from_ptr = 0
        while len(frontier_2) != 0:
            element = frontier_2.pop()
            print(f"Max dist so far: {max_dist_from_ptr}, node: {element[0].val}, current dist: {dist_from_ptr}")
            if max_dist_from_ptr < dist_from_ptr:
                max_dist_from_ptr = dist_from_ptr
                endpoint = element[0]
            element[0].visited = True
            if element[0].parent != None and element[0].parent.visited == False:
                dist_from_ptr = element[1] + 1
                frontier_2.append([element[0].parent, dist_from_ptr])
            
            if element[0].right != None and element[0].right.visited == False:
                dist_from_ptr = element[1] + 1
                frontier_2.append([element[0].right, dist_from_ptr])
            
            if element[0].left != None and element[0].left.visited == False:
                dist_from_ptr = element[1] + 1
                frontier_2.append([element[0].left, dist_from_ptr])
        
        
        return max_dist_from_ptr
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