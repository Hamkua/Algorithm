from collections import deque 
import sys 
input = sys.stdin.readline 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  data[x][y] = 0
  w = 1
  while queue:
    
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m:
        if data[nx][ny] == -1:
          data[nx][ny] = 0
          w += 1
          queue.append((nx,ny))

  return w

m,n,k = map(int, input().split())
data = [[-1]*m for _ in range(n)]
count = 0
result = []

for _ in range(k):
  sx,sy,ex,ey = map(int,input().split())
  for i in range(sx,ex):
    for j in range(sy,ey):
      data[i][j] = -2
  
for i in range(n):
  for j in range(m):
    if data[i][j] == -1:
      
      w = bfs(i,j)
      result.append(w)
      count += 1
      
print(count)
result.sort()
for i in result:
  print(i, end=" ")
