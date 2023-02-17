

def minScore(n, roads):

    def find_children(node, roads):
        children = list()
        for i in range(len(roads)):
            if node == roads[i][0]or node == roads[i][1]:
                children.append(roads[i])
        return children
    opt_cost = 1e9
    frontier = list()
    children_list = find_children(1, roads)
    for child in children_list:
        if child[2] < opt_cost:
            opt_cost = child[2]
    frontier.extend(children_list)
    i = 0
    while len(frontier) - 1 >= i:
        # print(f"Frontier: {frontier}")
        # print(len(frontier), i)
        a = frontier[i][0]
        b = frontier[i][1]
        i += 1
        child1_list = find_children(a, roads)
        child2_list = find_children(b, roads)
        child1_list.extend(child2_list)
        for child in child1_list:
            if child not in frontier:
                frontier.append(child)
                if child[2] < opt_cost:
                    opt_cost = child[2]
    return opt_cost

roads = [[12,7,2151],[7,2,7116],[11,14,8450],[11,2,9954],[1,11,3307],[10,7,3561],[10,1,4986],[11,7,7674],[14,2,1764],[11,12,6608],[14,7,1070],[9,8,2287],[14,12,6559],[1,2,1450],[2,12,9165]]
print(minScore(3, roads))