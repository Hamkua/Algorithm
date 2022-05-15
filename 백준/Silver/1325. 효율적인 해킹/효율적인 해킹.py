from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
  visited = [False]*(n+1)
  visited[start] = True
  count = 0
  queue = deque()
  queue.append(start)

  while queue:
    q = queue.popleft()
    count += 1
    for d in data[q]:
      if visited[d] == False:
        visited[d] = True
        queue.append(d)
  return count

n, m = map(int,input().split())
data = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int,input().split())
  data[b].append(a)
max_cnt = 0
result = []

for i in range(1,n+1):
  if data[i]:
    temp = bfs(i)
    if max_cnt <= temp:
      if max_cnt < temp:
        result = []
      max_cnt = temp
      result.append(i)

for i in result:
  if i:
    print(i,end=" ")