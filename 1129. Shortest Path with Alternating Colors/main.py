import collections

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        # BFS
        def find_children(redEdges, blueEdges):
            # 0 is red
            # 1 is blue
            children = collections.defaultdict(lambda: [])
            for i in range(len(redEdges)):
                children[redEdges[i][0]].append([redEdges[i][1], 0])
            for j in range(len(blueEdges)):
                children[blueEdges[j][0]].append([blueEdges[j][1], 1])
            return children
        
        dict_children = find_children(redEdges, blueEdges)
        
        visited_red = [False for i in range(n)]
        visited_blue = [False for i in range(n)]
        min_dist = [-1 for i in range(n)]
        frontier = collections.deque()
        frontier.append([0, 0, -1])
        
        while len(frontier) != 0:
            element = frontier.popleft()
            if min_dist[element[0]] == -1:
                min_dist[element[0]] = element[1]
            children_list = dict_children[element[0]]
            for i in range(len(children_list)):
                if element[2] == 1 or element[2] == -1:
                    if children_list[i][1] == 0 and visited_red[children_list[i][0]] == False: # red
                        visited_red[children_list[i][0]] = True
                        frontier.append([children_list[i][0], element[1]+1, 0])
                if element[2] == 0 or element[2] == -1:
                    if children_list[i][1] == 1 and visited_blue[children_list[i][0]] == False: # blue
                        visited_blue[children_list[i][0]] = True
                        frontier.append([children_list[i][0], element[1]+1, 1])
        return min_dist

if __name__ == "__main__":
    n = 3
    redEdges = [[0,1],[0,2]]
    blueEdges = [[1,0]]
    sol = Solution()
    print(sol.shortestAlternatingPaths(n, redEdges, blueEdges))
        