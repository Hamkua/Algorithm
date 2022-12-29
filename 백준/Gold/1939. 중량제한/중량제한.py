import heapq
from collections import defaultdict
import sys 
input = sys.stdin.readline 

n, m = map(int, input().strip().split())
data = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().strip().split())
  data[a].append((-1 * c, b))
  data[b].append((-1 * c, a))

start, end = map(int, input().strip().split())

def dijkstra(start):

  result = defaultdict(int)
  heap = []
  heapq.heappush(heap, ( -1 * sys.maxsize, start))

  while(heap):
    weight, destination = heapq.heappop(heap)

    if(result[destination] < weight):
      continue
      
    for next_weight, next_destination in data[destination]:
      
      min_weight = max(weight, next_weight)
      if(result[next_destination] > min_weight):
        # print(destination, weight, next_destination, next_weight)
        result[next_destination] = min_weight
        heapq.heappush(heap, ( min_weight, next_destination))

  return result[end]


print(-1 * dijkstra(start))