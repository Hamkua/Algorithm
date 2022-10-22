import heapq
import sys

input = sys.stdin.readline

def prim():
  result = 0
  heap = []
  for edge, end in data[1]:
    heapq.heappush(heap, (edge, end))

  while(heap):
    edge, end = heapq.heappop(heap)
    
    if(visited[end] == 0):
      result += edge
      visited[end] = 1

      for i in data[end]:
        heapq.heappush(heap, i)

    if sum(visited) == v:
      return result
v, e = map(int, input().strip().split())
visited = [0 for _ in range(v + 1)]
visited[1] = 1
data = [[] for _ in range(v + 1)]

for _ in range(e):
  a, b, c = map(int, input().strip().split())
  data[a].append((c, b))
  data[b].append((c, a))

print(prim())