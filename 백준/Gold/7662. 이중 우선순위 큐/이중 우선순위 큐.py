import heapq
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  min_value = 2147483647
  max_value = -2147483648
  done = set()
  minh = []
  maxh = []
  n = int(input())
  for i in range(n):
    a,b = input().strip().split()
    b = int(b)
    if(a == "I"):
      heapq.heappush(minh, (b, i))
      heapq.heappush(maxh, (-1*b, i))

    else:
      if(b == -1):
        while(minh):
          tmp, tmp_index = heapq.heappop(minh)
          if(tmp_index in done):
            continue
          else:
            done.add(tmp_index)
            break
            
      elif(b == 1):
        while(maxh):
          tmp, tmp_index = heapq.heappop(maxh)
          if(tmp_index in done):
            continue
          else:
            done.add(tmp_index)
            break
  
  while(maxh):
    tmp, tmp_index = heapq.heappop(maxh)
    if(tmp_index in done):
      continue
    else:
      max_value = max(-tmp, max_value)
 
  while(minh):
    tmp, tmp_index = heapq.heappop(minh)
    if(tmp_index in done):
      continue
    else:
      min_value = min(tmp, min_value)
    
  if(max_value == -2147483648 and min_value == 2147483647):
    print("EMPTY")
  else:
    print("{} {}".format(max_value, min_value))