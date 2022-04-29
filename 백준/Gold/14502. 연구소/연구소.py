from collections import deque

result = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
graph = []
temp = [[0]*m for _ in range(n)]

for _ in range(n):
  graph.append(list(map(int,input().split())))

def virus(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      if temp[nx][ny]==0:
        temp[nx][ny] = 2
        queue.append((nx,ny))
  
def bfs(count):
  global result
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = graph[i][j]

    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i,j)

    score = 0
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 0:
          score += 1
    result = max(result, score)
    return

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        count += 1
        bfs(count)
        graph[i][j] = 0
        count -= 1

bfs(0)
print(result)