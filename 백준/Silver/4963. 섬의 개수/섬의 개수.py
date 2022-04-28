import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0,-1,1,1,-1]
dy = [0,0,-1,1,1,-1,1,-1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  while queue:
    x,y = queue.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or nx>=h or ny<0 or ny>=w:
        continue
      if graph[nx][ny]==1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))
  
while (1):
  count = 0
  w,h = map(int,input().split())
  if (w==0 and h==0):
    break
  graph = [list(map(int,input().split())) for _ in range(h)]
  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        bfs(i,j)
        count += 1
  print(count)