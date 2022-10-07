from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
  queue= deque()

  for i in range(m):
    for j in range(n):
      if graph[i][j] == 1:
        queue.append((i,j))

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx<0 or ny<0 or nx>=m or ny>=n:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx,ny))
      
n,m = map(int,input().split())
result = 0

graph = []
for _ in range(m):
  graph.append(list(map(int,input().split())))
bfs()
for g in graph:
  for gg in g:
    if gg == 0:
      print(-1)
      exit()
  result = max(result,max(g)-1)
print(result)
