import sys
import heapq 
from itertools import permutations
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
      if(edge <= INF):
        next_edge = edge + current_edge
        if(result[node] > next_edge):
          result[node] = next_edge
          heapq.heappush(heap, (next_edge, node))

  return result
  
n, e = map(int, input().strip().split())
data = [[] for _ in range(n + 1)]

for _ in range(e):
  a, b, c = map(int, input().strip().split())
  data[a].append((c, b))
  data[b].append((c, a))

v1, v2 = map(int, input().strip().split())


start_result = dijkstra(1)
v1_result = dijkstra(v1)
v2_result = dijkstra(v2)


answer = min(start_result[v1] + v1_result[v2] + v2_result[n], start_result[v2] + v2_result[v1] + v1_result[n])
print(answer if answer < INF else -1)