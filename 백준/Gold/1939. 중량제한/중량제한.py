import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
  visited = defaultdict(int)
  
  heap = []
  heapq.heappush(heap, ( -1 * INF, start))

  while(heap):
    weight, destination = heapq.heappop(heap)
    if visited[destination] < weight:
      continue
    else:
        
      for next_weight, next_destination in data[destination]:
        min_weight = max(weight, next_weight)
        if visited[next_destination] > min_weight:
          visited[next_destination] = min_weight
          heapq.heappush(heap, (min_weight, next_destination))

      # print(visited)
  return visited[end]
      
  

n, m = map(int, input().strip().split())
data = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, c = map(int, input().strip().split())

  data[a].append((-1 * c, b))
  data[b].append((-1 * c, a))

start, end = map(int, input().strip().split())

print(-1 * dijkstra(start))

# 9 9
# 1 4 11
# 1 5 2
# 4 5 4
# 4 3 10
# 4 2 7
# 5 2 10
# 5 6 13
# 3 2 9
# 2 6 8
# 1 6 
# -> 9