from collections import deque
import sys

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(ax,ay):
  
  queue = deque()
  queue.append((ax,ay))
  visited[ax][ay] = 0

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m:
        if visited[nx][ny]== -1 and data[nx][ny] == 'L':
          queue.append((nx,ny))
          visited[nx][ny] = visited[x][y]+1   
  return visited[x][y]

n,m = map(int,input().split())
data =[]
for _ in range(n):
  data.append(list(input().rstrip()))

max_num = 0
for i in range(n):
  for j in range(m):
    if data[i][j] == 'L':
      visited = [[-1]*m for _ in range(n)]
      num = bfs(i,j)
      max_num = max(num,max_num)

print(max_num)