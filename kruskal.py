def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

def kruskals_mst(edges, nodes):
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}
    mst = []
    cost = 0

    edges.sort(key=lambda x: x[2])  # sort by weight

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, w))
            cost += w

    print("\nEdges in MST:")
    for u, v, w in mst:
        print(f"{u} - {v} : {w}")
    print(f"Total cost of MST using Kruskal's Algorithm: {cost}")

edges = []
nodes = set()
n = int(input("Enter number of edges: "))
print("Enter edges in the format: node1 node2 weight")

for _ in range(n):
    u, v, w = input().split()
    w = int(w)
    edges.append((u, v, w))
    nodes.update([u, v])

kruskals_mst(edges, nodes)
