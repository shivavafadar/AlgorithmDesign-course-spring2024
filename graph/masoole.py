import heapq

def dijkstra(n, graph, start):
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def count_puzzle_pieces(n, m, s, roads, d):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    distances = dijkstra(n, graph, s)
    
    puzzle_pieces = 0
    
    for node, distance in distances.items():
        if distance == d:
            puzzle_pieces += 1
    
    for u, v, w in roads:
        du = distances[u]
        dv = distances[v]
        if du < d < dv and du + w >= d:
            puzzle_pieces += 1
        elif dv < d < du and dv + w >= d:
            puzzle_pieces += 1
    
    return puzzle_pieces

# Reading input
n, m, s = map(int, input().split())
roads = []
for _ in range(m):
    u, v, w = map(int, input().split())
    roads.append((u, v, w))
d = int(input())

# Calculating the number of puzzle pieces
result = count_puzzle_pieces(n, m, s, roads, d)
print(result)
