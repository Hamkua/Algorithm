import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
data = defaultdict(list)

for _ in range(m):
  a, b, c = map(int, input().strip().split())
  data[a].append((c, b))
  data[b].append((c, a))

visited = [0] * (n + 1)
visited[1] = 1

heap = []
for i in data[1]:
  heapq.heappush(heap, i)

result = 0
cnt = 1
max_edge = -1
while(heap):
  edge, destination = heapq.heappop(heap)

  if visited[destination] == 0:
    max_edge = max(max_edge, edge)
    cnt += 1
    visited[destination] = 1
    result += edge

    for i in data[destination]:
      if visited[i[1]] == 0:
        heapq.heappush(heap, i)

  else:
    continue

  if cnt == n:
    print(result - max_edge)
    break
  