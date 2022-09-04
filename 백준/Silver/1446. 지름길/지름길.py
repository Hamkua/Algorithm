import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start, end):
  heap = []
  heapq.heappush(heap, (0, start))

  result = [INF] * (end + 1)
  result[start] = 0

  while(heap):
    edge, location = heapq.heappop(heap)

    if result[location] < edge:
      continue
      
    for current_location, current_edge in data[location]:

      next_edge = edge + current_edge
      if result[current_location] > next_edge:
        result[current_location] = next_edge
        heapq.heappush(heap, (next_edge, current_location))

  # print(result)
  return result[end]
        
n, d = map(int, input().strip().split())
data = [[] for _ in range(d + 1)]

for i in range(d):
  data[i].append((i + 1, 1))

for _ in range(n):
  start, end, edge = map(int, input().strip().split())

  if end > d:
    continue

  data[start].append((end, edge))

print(dijkstra(0, d))
