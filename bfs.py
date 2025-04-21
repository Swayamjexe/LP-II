from collections import deque
def bfs(graph, start):  
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
# User input
graph = {}
n = int(input("Enter number of edges: "))
for i in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)  # Undirected graph

start_node = input("Enter starting node for BFS: ")
print("BFS Traversal:")
bfs(graph, start_node)
# time complexity = O(V + E) where V is the number of vertices and E is the number of edges.
# space complexity = O(V) for the visited set and queue