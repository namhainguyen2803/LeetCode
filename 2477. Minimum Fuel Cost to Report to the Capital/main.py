import collections
import copy
import math
class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        def children(roads):
            dic = collections.defaultdict(lambda: [])
            for edge in roads:
                dic[edge[0]].append(edge[1])
                dic[edge[1]].append(edge[0])
            return dic
        
        children_dict = children(roads)
        num_vertices = len(roads) + 1
        
        level_dict = collections.defaultdict()
        level_dict[0] = 0
        
        predecessor_list = [0 for i in range(num_vertices)]
        
        visited = [False for i in range(num_vertices)]
        visited[0] = True
        
        frontier = collections.deque()
        frontier.append([0, 0])
        explored_set = list()
        
        while len(frontier) != 0:
            element = frontier.popleft()
            explored_set.append(element)
            # print(element)
            children_element = children_dict[element[0]]
            for i in range(len(children_element)):
                if visited[children_element[i]] == False:
                    visited[children_element[i]] = True
                    predecessor_list[children_element[i]] = element[0]
                    frontier.append([children_element[i], element[1]+1])
                    level_dict[children_element[i]] = element[1]+1
        
        # print(predecessor_list)
        # print(level_dict)
        # print(explored_set)
        
        demo = copy.deepcopy(explored_set)
        degree = [1 for i in range(num_vertices)]

        while len(demo) != 0:
            d = demo.pop()
            if d[0] != 0:
                degree[predecessor_list[d[0]]] += degree[d[0]]
        
        # print(degree)
        
        visited_2 = [False for i in range(num_vertices)]
        visited_2[0] = True
        visited_3 = [False for i in range(num_vertices)]
        visited_3[0] = True
        total_cost = 0
        
        while len(explored_set) != 0:
            if visited_2[explored_set[-1][0]] == True:
                remove_element = explored_set.pop()
            else:
                # current_seat = 1
                cost = 0
                frontier_2 = list()
                frontier = collections.deque()
                frontier.append(explored_set[-1][0])
                tour = list()
                frontier_2.append(explored_set[-1][0])
                tour.append(explored_set[-1][0])
                visited_2[explored_set[-1][0]] = True
                element = explored_set[-1][0]
                
                
                while len(tour) < seats and len(frontier) != 0:
                    element = frontier.pop()
                    if element == 0:
                        tour.append(element)
                        break
                    else:
                        children_list = children_dict[element]
                        
                        if element not in tour and visited_3[element] == False:
                            
                            tour.append(element)
                            if element not in frontier_2:
                                frontier_2.append(element)
                            visited_3[element] = True
                            
                        if len(tour) == seats:
                            break
                        for child in children_list:
                            if visited_2[child] == False:
                                if child == 1 and element == 2:
                                    print(tour)
                                    print(degree[child] - degree[element], element, child, seats - len(tour))
                                if child == predecessor_list[element] and (degree[child] - degree[element]) <= (seats - len(tour)):
                                    # cost += 1
                                    frontier.append(child)
                                    visited_2[child] = True
                                if child != predecessor_list[element]:
                                    if (degree[child] % seats) <= (seats - len(tour)):
                                        frontier.append(child)
                                        visited_2[child] = True
                            else:
                                if child not in tour and child == predecessor_list[element]:
                                    frontier.append(child)
                                    cost += 1
                                    if child not in frontier_2:
                                        frontier_2.append(child)
                                    # print(child, cost)
                

                

                min_level = 1e9
                for t in frontier_2:
                    if t >=0:
                        if t == 0:
                            min_level = 0
                            break
                        if min_level > level_dict[t]:
                            min_level = level_dict[t]
                            
                print(tour, len(frontier_2)-1+min_level, len(tour))
                # for t in tour:
                #     print(t, level_dict[t])
                total_cost += (len(frontier_2)-1+min_level)
                
        
        return total_cost
                            
        
class Solution_2:
    def minimumFuelCost(self, roads, seats):
    	# Build the graph, since it is undirected, we add both directions
        graph = collections.defaultdict(list)
        for c1,c2 in roads:
            graph[c1].append(c2)
            graph[c2].append(c1)
        res = 0
        def dfs(node,par):
            nonlocal res
            totalPeople = 1

            for nei in graph[node]:
                if nei != par:
                    people, car = dfs(nei,node)
                    totalPeople += people
                    res += car
            cars = math.ceil(totalPeople/seats)
            return totalPeople,cars

        print(dfs(0,None))
        return res
    
if __name__ == "__main__":
    roads = [[0,1], [1,2], [2,3], [2,5], [3,4], [5,6], [0,7], [7,8], [8,9], [8,11], [9,10], [11,12], [12,13], [13,14],[14,15],[15,16],[10,17]]
    roads_2 = [[0,1],[0,2],[1,3],[1,4]]
    roads_3 = [[0,1],[0,2],[3,2],[0,4],[1,5],[5,6],[3,7]]
    roads_4 = [[0,1],[0,2],[1,3],[3,4],[0,5],[6,3],[5,7],[3,8]]
    roads_5 = [[0,1],[1,2],[1,3],[4,2],[5,3],[6,3],[6,7],[8,6],[9,0],[5,10],[11,9],[12,5],[5,13],[8,14],[11,15],[8,16],[17,0],[18,7]] # seats = 13, expect = 19
    roads_6 = [[0,1],[2,0],[3,2],[3,4],[2,5],[6,4],[6,7],[8,2],[9,0],[3,10],[1,11],[5,12],[6,13],[6,14],[15,10],[16,0],[14,17],[12,18],[19,6],[20,17],[14,21],[12,22],[23,20],[24,11],[25,15],[26,7],[17,27],[15,28],[5,29],[30,8],[31,1],[32,12],[33,29],[34,5],[35,27],[36,30],[37,31],[20,38],[16,39],[40,6],[28,41],[42,30],[43,2],[12,44],[45,17],[5,46],[47,6]] # seats=26, expect=48
    roads_7 = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]] # seats=2, expect=7
    roads_8 = [[0,1],[2,1],[3,2],[4,2],[4,5],[6,0],[5,7],[8,4],[9,2]]
    roads_9 = [[1,0],[1,2],[3,2],[2,4],[5,3],[6,1],[6,7],[8,1],[1,9],[10,5],[11,3],[12,3],[13,3],[2,14],[3,15],[14,16],[0,17],[2,18],[18,19],[14,20],[0,21],[12,22],[19,23],[0,24],[25,17],[5,26],[27,15],[28,27],[12,29],[30,29],[31,8],[9,32],[33,10],[34,29],[23,35],[17,36],[28,37],[38,26],[39,37],[40,9],[41,9],[6,42],[15,43],[24,44],[17,45],[24,46]] # seats=33, expect=47
    seats = 33
    sol = Solution()
    sol_2 = Solution_2()
    # print(sol_2.minimumFuelCost(roads_9, seats))
    print(sol.minimumFuelCost(roads_9, seats))
            