import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
  heapq.heappush(heap, (0, start))

  while(heap):
    edge, node = heapq.heappop(heap)

    if(result[node] < edge):
      continue

    else:
      for next_edge, next_node in data[node]:
        total_edge = edge + next_edge
        if(result[next_node] > total_edge):
          result[next_node] = total_edge
          heapq.heappush(heap, (total_edge, next_node))
      
t = int(input())

for _ in range(t):
  heap = []
  time = 0
  cnt = 0
  
  n, d, c = map(int, input().strip().split())

  result = [INF]*(n + 1)
  result[c] = 0
  data = [[] for _ in range(n + 1)]
  
  for _ in range(d):
    a, b, s = map(int, input().strip().split())
    data[b].append((s, a))

  dijkstra(c)

  for r in result:
    if r != INF:
      cnt += 1
      if(time < r):
        time = r
  
  print(cnt, end = " ")
  print(time)