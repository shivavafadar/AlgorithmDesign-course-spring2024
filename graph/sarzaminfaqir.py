class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst_edges = []
    
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u, v, weight))
    
    return mst_edges

def will_road_be_in_mst(n, mst_edges, new_road, original_edges):
    u, v, weight = new_road
    
    # Check if adding the new road creates a cycle
    uf = UnionFind(n)
    for x, y, w in mst_edges:
        uf.union(x, y)
    
    if uf.find(u) != uf.find(v):
        return True
    
    # If it creates a cycle, check if it's the lightest edge in the cycle
    # Reconstruct the graph to find the cycle
    graph = {i: [] for i in range(n)}
    for x, y, w in mst_edges:
        graph[x].append((y, w))
        graph[y].append((x, w))
    
    # Perform BFS or DFS to find the cycle
    def find_cycle(graph, start, end, weight):
        stack = [(start, [start], 0)]
        visited = set()
        
        while stack:
            node, path, max_weight = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            
            for neighbor, w in graph[node]:
                if neighbor == end:
                    return max(max_weight, w)
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], max(max_weight, w)))
        return float('inf')
    
    max_edge_in_cycle = find_cycle(graph, u, v, weight)
    
    return weight < max_edge_in_cycle

# Reading input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
q = int(data[2])

edges = []
index = 3
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    w = int(data[index + 2])
    edges.append((u - 1, v - 1, w))
    index += 3

queries = []
for _ in range(q):
    u = int(data[index])
    v = int(data[index + 1])
    w = int(data[index + 2])
    queries.append((u - 1, v - 1, w))
    index += 3

# Calculate the initial MST
mst_edges = kruskal(n, edges)

# Process each query
results = []
for new_road in queries:
    if will_road_be_in_mst(n, mst_edges, new_road, edges):
        results.append("Yes")
    else:
        results.append("No")

# Print results
for result in results:
    print(result)
