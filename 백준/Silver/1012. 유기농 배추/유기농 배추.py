from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while(queue):
    x,y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx<0 or ny<0 or nx>=n or ny >=m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx,ny))

  return graph[n-1][m-1]

t = int(input())

for _ in range(t):
  n,m,p = map(int,input().split())
  graph = [[0]*m for _ in range(n)]

  for _ in range(p):
    ax,ay = map(int,input().split())
    graph[ax][ay] = 1
  result =0

  for i in range(n):
    for j in range(m):
      if graph[i][j]==1:
        bfs(i,j)
        result+=1
  print(result)
