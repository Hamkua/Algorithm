import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
heap = []

n = int(input())
m = int(input())

result = [INF] * (n + 1)
route = [[] for _ in range(n + 1)]
data = [[] for _ in range(n + 1)]

for _ in range(m):
  from_node, to_node, edge = map(int, input().strip().split())
  data[from_node].append((edge, to_node))


start, end = map(int, input().strip().split())

heapq.heappush(heap, (0, start))
result[start] = 0
route[start].append(start)

while(heap):
  weight, destination = heapq.heappop(heap)

  if(result[destination] < weight):
    continue
  else:
    for next_weight, next_destination in data[destination]:
      total_weight = weight + next_weight
      if(result[next_destination] > total_weight):
        result[next_destination] = total_weight
        heapq.heappush(heap, (total_weight, next_destination))
        route[next_destination] = []
        for r in route[destination]:
          route[next_destination].append(r)
  
        route[next_destination].append(next_destination)

print(result[end])
print(len(route[end]))
print(" ".join(map(str, route[end])))