import sys
import heapq
input = sys.stdin.readline

n = int(input())
positive_heap = []
negative_heap = []

for i in range(n):
  num = int(input().strip())
  if(num == 0):
    if(positive_heap and negative_heap):
      if(positive_heap[0] >= negative_heap[0]):
        result = -1 * heapq.heappop(negative_heap)
      else:
        result = heapq.heappop(positive_heap)

    elif(positive_heap):
      result = heapq.heappop(positive_heap)
    elif(negative_heap):
      result = -1 * heapq.heappop(negative_heap)
    else:
      result = 0
    print(result)    
  else:
    if(num < 0):
      heapq.heappush(negative_heap, -1 * num)
    else:
      heapq.heappush(positive_heap, num)