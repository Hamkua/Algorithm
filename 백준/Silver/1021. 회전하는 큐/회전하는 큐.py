from collections import deque
import sys
import copy
input = sys.stdin.readline


n,m = map(int,input().strip().split())
data = list(map(int,input().strip().split()))

queue = deque([i for i in range(1, n+1)])

cnt = 0

for i in range(m):
  while(queue):
    q = queue.popleft()
 
    if q == data[i]:
      break

    queue.appendleft(q)
    idx = queue.index(data[i])
    
    if (len(queue) - idx) > idx:
      queue.rotate(-1)
      cnt += 1
      continue

    else:
      queue.rotate(1)
      cnt += 1
      continue
        
print(cnt)