import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
  result = [INF] * (n + 1)
  result[start] = 0
  heap = []

  heapq.heappush(heap, (0, start))
  while(heap):
    current_edge, current_node = heapq.heappop(heap)
    for edge, node in data[current_node]:
      if edge < INF:
        next_edge = edge + current_edge
        if result[node] > next_edge:
          result[node] = next_edge
          heapq.heappush(heap, (next_edge, node))

  return result

n, m, x = map(int, input().strip().split())

data = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().strip().split())
  data[a].append((c, b))

max_edge = 0
back_route = dijkstra(x)

for i in range(1, n + 1):
  if i != x:
    front_route = dijkstra(i)
    max_edge = max(max_edge, front_route[x] + back_route[i])

print(max_edge)