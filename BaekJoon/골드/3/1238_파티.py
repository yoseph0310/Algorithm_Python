import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
INF = sys.maxsize
graph = [[] for _ in range(N + 1)]
rev_graph = [[] for _ in range(N + 1)]
heap = []

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])
    rev_graph[e].append([w, s])

def dijkstra(start, graph):
    distances = [INF] * (N + 1)
    distances[start] = 0
    heapq.heappush(heap, [0, start])    # 비용 노드

    while heap:
        dist, node = heapq.heappop(heap)
        if distances[node] < dist:
            continue

        for n_dist, n_node in graph[node]:
            cost = n_dist + dist
            if distances[n_node] > cost:
                distances[n_node] = cost
                heapq.heappush(heap, [cost, n_node])

    return distances

ans = 0
go_d = dijkstra(X, graph)
back_d = dijkstra(X, rev_graph)

for i in range(1, N+1):
    ans = max(ans, go_d[i] + back_d[i])

print(ans)