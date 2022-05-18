from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
  size = 1
  visited[x][y] = True
  queue = deque()
  queue.append((x,y))

  while(queue):
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if(0<=nx<m and 0<=ny<n):
        if(visited[nx][ny] == False and graph[nx][ny] == 0):
          visited[nx][ny] = True
          queue.append((nx,ny))
          size += 1

  return size 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m,n,k = map(int,input().strip().split())

graph = [[0]*(n+1) for _ in range(m+1)]
visited = [[False]*(n+1) for _ in range(m+1)]
cnt = 0
result = []

for _ in range(k):
  start_y, end_x, end_y, start_x = map(int, input().strip().split())

  start_x = m - start_x
  end_x = m - end_x
  for i in range(start_x, end_x):
    for j in range(start_y, end_y):
      graph[i][j] = 1


for i in range(m):
  for j in range(n):
    if graph[i][j] == 0 and visited[i][j] == False:
      result.append(bfs(i,j))
      cnt += 1

result.sort()
print(cnt)
for size in result:
  print(size, end=" ")