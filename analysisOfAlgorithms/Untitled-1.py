def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]

def union(parent, vertex1, vertex2):
    parent[find(parent, vertex1)] = find(parent, vertex2)

def kruskals_algorithm(vertices, edges):
    mst = []
    edges.sort(key=lambda x: x[2])
    parent = {vertex: vertex for vertex in vertices}
    for edge in edges:
        vertex1, vertex2, weight = edge
        if find(parent, vertex1) != find(parent, vertex2):
            mst.append(edge)
            union(parent, vertex1, vertex2)
    return mst

vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B', 2), ('A', 'D', 4), ('B', 'C', 3), ('B', 'D', 1), ('C', 'D', 5)]
print("Kruskal's Algorithm:", kruskals_algorithm(vertices, edges))