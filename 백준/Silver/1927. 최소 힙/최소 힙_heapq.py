import sys
import heapq

input = sys.stdin.readline

heap = []
n = int(input())

for i in range(n):
  x = int(input())
  if(x == 0):
    if(len(heap) == 0):
      print(0)
    else:
      r = heapq.heappop(heap)
      print(r)
  else:
    heapq.heappush(heap, x)