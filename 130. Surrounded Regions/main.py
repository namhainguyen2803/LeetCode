class Node:
    def __init__(self, row=None, col=None):
        self.parent = [row, col]
        self.rank = 0
        self.coordinate = [row, col]
        
class DisjointSet:
    def find_set(self, x):
        if x.coordinate != x.parent:
            x.parent = self.find_set(x.parent)
        return x
    def union(self, x, y):
        p_x = self.find_set(x)
        p_y = self.find_set(y)
        if p_x.rank > p_y.rank:
            p_y.parent = p_x
        else:
            p_x.parent = p_y
            if p_x.rank == p_y.rank:
                p_y.rank += 1


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        list_node = [[Node(i, j) for j in range(len(board))] for i in range(len(board))]
        disjoint_set = DisjointSet()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == "O":
                    if row > 0 or col > 0:
                        if board[row-1][col] == "O":
                            disjoint_set.union(list_node[row][col], list_node[row-1][col])
                        if board[row][col-1] == "O":
                            disjoint_set.union(list_node[row][col], list_node[row][col-1])
        print(board[2][2])
        print(disjoint_set.find_set(list_node[2][2]).parent)

cls = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
cls.solve(board)