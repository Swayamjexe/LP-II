import heapq
def a_star_algorithm(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristics[start], 0, start, [start]))  # (f(estimated), g(total), current, path)
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


# Enter number of edges: 6
# Enter edges in the format 'u v cost' (e.g., A B 4):
# A B 1
# A C 4
# B D 2
# C D 5
# B E 3
# D E 1

# Enter heuristic (estimated cost to goal) for each node:
# Heuristic for A: 7
# Heuristic for B: 6
# Heuristic for C: 5
# Heuristic for D: 3
# Heuristic for E: 0

# Enter start node: A
# Enter goal node: E

