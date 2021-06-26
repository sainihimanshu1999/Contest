'''
In this question we have to find the cycles in the graph and we can do this by two methods, one is or dfs algorithm
and other is of disjoint set algorithm
'''
from collections import defaultdict

#DFS O(N^2) time complexity
def redundantConnection(edges):
    graph = defaultdict(set)

    for u,v in edges:
        visited = set()
        if dfs(graph,u,v,visited):
            return [u,v]

        graph[u].add(v)
        graph[v].add(u)


def dfs(graph,u,v,visited):
    if u == v: return True

    for node in graph[u]:
        if node not in visited:
            visited.add(node)
            if dfs(graph,node,v,visited):
                return True
    return False



#Disjoint Set Method i.e union find 


def redundantConnection2(edges):
    parent = [0]*len(edges)

    def find(x):
        if not parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]


    def union(x,y):
        rootX = find(x)
        rootY = find(y)

        if rootX == rootY:
            return False

        parent[rootX] = rootY
        return True


    for u,v in edges:
        if not union(u-1,v-1):
            return [u,v]


edges = [[1,2],[1,3],[2,3]]
print(redundantConnection2(edges))



        
