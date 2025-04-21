import heapq
def prims_mst(graph, start):
    visited = set()
    min_heap = [(0, start)]
    total_cost = 0
    mst = []

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            total_cost += cost

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))
                    mst.append((node, neighbor, weight))

    print("\nEdges in MST:")
    for u, v, w in mst:
        if u in visited and v in visited:
            print(f"{u} - {v} : {w}")
    print(f"Total cost of MST using Prim's Algorithm: {total_cost}")

graph = {}
n = int(input("Enter number of edges: "))
print("Enter edges in the format: node1 node2 weight")
for i in range(n):
    u, v, w = input().split()
    w = int(w)
    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))  # because it's undirected

start_node = input("Enter starting node: ")
prims_mst(graph, start_node)
