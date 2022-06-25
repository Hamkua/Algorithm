import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
heap = []

def dijkstra(start, end):
  heapq.heappush(heap, (0, start))
  result[start] = 0
  while(heap):
    cost, destination = heapq.heappop(heap)

    if(result[destination] < cost):
      continue 
    else: 
      for next_cost, next_destination in data[destination]:
        new_cost = cost + next_cost
        if result[next_destination] > new_cost:
          result[next_destination] = new_cost
          heapq.heappush(heap, (new_cost, next_destination))
        
n = int(input())
m = int(input())


data = [[] for _ in range(n + 1)]
result = [INF] * (n + 1)

for _ in range(m):
  f, t, cost = map(int, input().strip().split())
  data[f].append((cost, t))
    
# for i in range(n + 1):
#   print(data[i])

start, end = map(int, input().strip().split())
dijkstra(start, end)
print(result[end])