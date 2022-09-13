import sys
import heapq 

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
  result = [INF] * (n + 1)
  
  result[start] = 0

  heap = []
  heapq.heappush(heap, (0, start))

  while(heap):
    previous_edge, previous_location = heapq.heappop(heap)

    for current_edge, current_location in data[previous_location]:
      next_edge = previous_edge + current_edge

      if result[current_location] > next_edge:
        result[current_location] = next_edge
        heapq.heappush(heap, (next_edge, current_location))
        

  return result

for _ in range(int(input())):
  
  n, m, t = map(int, input().strip().split())
  data = [[] for _ in range(n + 1)]
  candidate = list()
  
  s, g, h = map(int, input().strip().split())

  for _ in range(m):
    start, end, edge = map(int, input().strip().split())

    # 양방향
    data[start].append((edge, end))
    data[end].append((edge, start))

  for _ in range(t):
    candidate.append(int(input()))
    
    
  start_result = dijkstra(s)

  
  if start_result[g] > start_result[h]:
    idx = g
  else:
    idx = h
    

  transfer_result = dijkstra(idx)
  result = []
  for candidate_location in candidate:
    if transfer_result[s] + transfer_result[candidate_location] == start_result[candidate_location]:
      result.append(candidate_location)

  result.sort()
  for result_value in result:
    print(result_value, end=" ")
  print()