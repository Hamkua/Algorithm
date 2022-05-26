from collections import deque 
import sys 
input = sys.stdin.readline 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  
  queue = deque()
  queue.append((x,y))
  visited[x][y] = 0
  a = 10000

  while queue:
    x,y = queue.popleft() 
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<n:
        if data[nx][ny] == 1 and visited[nx][ny] == -1 and visited[x][y] > 0:
          a = min(a,visited[x][y])

        if data[nx][ny] == 0 and visited[nx][ny] == -1:
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx,ny))

  if a!=10000:
    return a

def check(i,j):
  queue = deque()
  queue.append((i,j))
  
  while queue:
    x,y = queue.popleft() 
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<n:
        if data[nx][ny] == 1 and visited[nx][ny] == -1:
          visited[nx][ny] = -2
          queue.append((nx,ny))

n = int(input())
data = []
for _ in range(n):
  data.append(list(map(int,input().split())))

min_l = 10000

for i in range(n):
  for j in range(n):
    visited = [[-1]*n for _ in range(n)]
    if data[i][j] == 1:
      check(i,j)
      l = bfs(i,j)
      if l != None:
        min_l = min(l,min_l)

print(min_l)