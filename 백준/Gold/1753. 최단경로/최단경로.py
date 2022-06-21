import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline


heap = []
v, e = map(int, input().strip().split())

result = [INF] * (v + 1)

data = [[] for _ in range(v + 1)]

start = int(input())

for _ in range(e):
  f,t,w = map(int, input().strip().split())
  data[f].append((w, t))

heapq.heappush(heap, (0, start))
result[start] = 0

while(heap):
  weight, current_node = heapq.heappop(heap)

  if(result[current_node] < weight):
    continue
  else:
    for wei, node in data[current_node]:
      next_weight = wei + weight
      if(result[node] > next_weight):
        result[node] = next_weight
        heapq.heappush(heap, (next_weight, node))
     
for i in range(1, v+1):
  if(result[i] == INF):
    print("INF")
  else:
    print(result[i])
