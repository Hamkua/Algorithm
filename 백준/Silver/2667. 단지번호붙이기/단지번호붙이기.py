import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph=[list(map(int,input().rstrip())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


cnt = 0
data = []

def bfs(x,y):
  global max_value
  max_value = 0
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
      if graph[nx][ny]==1:
        graph[nx][ny] = graph[x][y] +1
        max_value += 1
        queue.append((nx,ny))
  if max_value == 0:
    return 1
  return max_value

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      m = bfs(i,j)
      data.append(m)
      cnt += 1
data.sort()
print(cnt)
for d in data:
  print(d)


  


