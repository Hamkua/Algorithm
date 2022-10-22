import heapq
import sys
input = sys.stdin.readline  
    
n = int(input())
m = int(input())

data = [[] for _ in range(n + 1)]
parents = [i for i in range(n + 1)]
visited = [0] * (n + 1)
visited[1] = 1
result = 0

for _ in range(m):
  a, b, edge = map(int, input().strip().split())
  if a == b:
    continue

  data[a].append((edge, b))
  data[b].append((edge, a))

heap = []
for i in data[1]:
  heapq.heappush(heap, i)

while(heap):
  # print(heap)
  edge, end = heapq.heappop(heap)
  

  if visited[end] == 0:
    
    visited[end] = 1
    result += edge

    # print(edge, end)
    for i in data[end]:
      heapq.heappush(heap, i)

    # 
    if sum(visited) == n:
      break

print(result)