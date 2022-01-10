import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())         # N : 학생 수 (노드), M : 도로 수 (간선), T : 시간 (가중치)
INF = sys.maxsize
graph = [[] for _ in range(N + 1)]
heap = []

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])

def dijkstra(start):
    distances = [INF for _ in range(N + 1)]
    distances[start] = 0
    heapq.heappush(heap, [0, start])

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
for i in range(1, N + 1):
    start = dijkstra(i)
    end = dijkstra(X)
    ans = max(ans, start[X] + end[i])

print(ans)