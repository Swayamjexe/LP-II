def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# User input
graph = {}
n = int(input("Enter number of edges: "))
for i in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)  # Undirected graph

start_node = input("Enter starting node for DFS: ")
print("DFS Traversal:")
dfs(graph, start_node)
# time complexity = O(V + E) where V is the number of vertices and E is the number of edges.
# space complexity = O(V) for the visited set and recursion stack