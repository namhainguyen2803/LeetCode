def minScore(n, roads):
    
    def find_children(n, roads):
        children = [[] for j in range(n+1)]
        for i in range(len(roads)):
            children[roads[i][0]].append([roads[i][1], roads[i][2]])
            children[roads[i][1]].append([roads[i][0], roads[i][2]])
        return children
    adjacent_list = find_children(n, roads)
    visited = [False for j in range(n+1)]
    opt_cost = 1e9
    frontier = list()
    children_list = adjacent_list[1]
    for child in children_list:
        if child[1] < opt_cost:
            opt_cost = child[1]
    frontier.extend(children_list)
    i = 0
    while len(frontier) - 1 >= i:
        # print(f"Frontier: {frontier}")
        # print(len(frontier), i)
        a = frontier[i][0]
        i += 1
        child1_list = adjacent_list[a]
        for child in child1_list:
            if visited[child[0]] == False:
                visited[child[0]] = True
                frontier.append(child)
            if child[1] < opt_cost:
                opt_cost = child[1]
    return opt_cost



roads = [[12,7,2151],[7,2,7116],[11,14,8450],[11,2,9954],[1,11,3307],[10,7,3561],[10,1,4986],[11,7,7674],[14,2,1764],[11,12,6608],[14,7,1070],[9,8,2287],[14,12,6559],[1,2,1450],[2,12,9165]]
print(minScore(14, roads))