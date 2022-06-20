from collections import deque
import sys
input = sys.stdin.readline 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
  queue = deque()
  visited = [[0]*m for _ in range(n)]

  side = [[0,0],[0,m-1],[n-1,0],[n-1,m-1]]
  for i,j in side:
    queue.append((i,j))
    visited[i][j] = 1
  cnt = 0
  count = 0

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m:
        if data[nx][ny] != 0:
          count += 1
          data[nx][ny] = 0
          visited[nx][ny] = visited[x][y] + 1
          cnt = visited[nx][ny]-1

        if data[nx][ny] == 0 and visited[nx][ny]==0:
          visited[nx][ny] = 1
          queue.append((nx,ny))
  return cnt,count
    
n,m = map(int,input().split())
lu = [0,0]
ru = [0,m-1]
ld = [n-1,0]
rd = [n-1,m-1]

data = []
for _ in range(n):
  data.append(list(map(int,input().split())))

result = 0
result2 = 0
for i in range(n):
  for j in range(m):
    if data[i][j] == 1:
      a,b = bfs()
      result += a
      if b == 0:
        break
      else:
        result2 = b

print(result) 
print(result2)