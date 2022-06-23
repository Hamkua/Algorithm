from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()

def check(i, j):
  queue.append((i, j))
  visited[i][j] = 0

  while(queue):
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if(0<=nx<n and 0<=ny<n):
        if(visited[nx][ny] == -1 and data[nx][ny] == 1):
          visited[nx][ny] = 0
          queue.append((nx, ny))

  # for i in range(n):
  #   print(visited[i])
  
def bfs(i, j):
  tmp = sys.maxsize
  queue.append((i, j))

  while(queue):
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if(0<=nx<n and 0<=ny<n):
        if(data[nx][ny] == 0 and visited[nx][ny] == -1):
          queue.append((nx,ny))
          visited[nx][ny] = visited[x][y] + 1

        if(data[nx][ny] == 1 and visited[nx][ny] == -1):
          tmp = min(tmp, visited[x][y])

  return tmp
  
n = int(input())
data = []

result = sys.maxsize

for _ in range(n):
  data.append(list(map(int, input().strip().split())))

for i in range(n):
  for j in range(n):
    visited = [[-1] * (n + 1) for _ in range(n + 1)]
    if(data[i][j] == 1 and visited[i][j] == -1):
      check(i, j)
      if(visited[i][j] == 0):
        tmp = bfs(i,j)
        result = min(result, tmp)

print(result)