import sys
from heapq import heappush, heappop
input = sys.stdin.readline

INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
distances = [INF] * (V + 1)
heap = []

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    distances[start] = 0
    heappush(heap, (0, start))

    while heap:
        dist, node = heappop(heap)

        if distances[node] < dist:
            continue

        for n_node, n_dist in graph[node]:
            cost = dist + n_dist
            if distances[n_node] > cost:
                distances[n_node] = cost
                heappush(heap, (cost, n_node))

dijkstra(K)
for i in range(1, V+1):
    print("INF" if distances[i] == INF else distances[i])