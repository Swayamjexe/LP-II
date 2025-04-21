import heapq
def a_star_algorithm(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristics[start], 0, start, [start]))  # (f, g, current, path)
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if current == goal:
            print("Path found:", ' → '.join(path))
            print("Total cost:", g)
            return

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                total_cost = g + cost
                estimated_cost = total_cost + heuristics[neighbor]
                heapq.heappush(open_list, (estimated_cost, total_cost, neighbor, path + [neighbor]))

    print("No path found.")

graph = {}
nodes = set()
n = int(input("Enter number of edges: "))
for i in range(n):
    u, v, cost = input("Enter edge (u v cost): ").split()
    cost = int(cost)
    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))  # Since it's undirected (optional)
    nodes.update([u, v])

heuristics = {}
print("Enter heuristic values for each node:")
for node in nodes:
    heuristics[node] = int(input(f"Heuristic for {node}: "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

a_star_algorithm(graph, heuristics, start, goal)
