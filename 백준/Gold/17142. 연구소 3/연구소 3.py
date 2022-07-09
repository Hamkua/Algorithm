from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def check():
  max_value = 0
  for i in range(n):
    for j in range(n):
      if(data[i][j] != 1 and visited[i][j] == -1):
        return -1
      else:
        if data[i][j] != 2 and visited[i][j] > max_value:
          max_value = visited[i][j]
        
  return max_value
  
def bfs():
  while(queue):
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if(0<=nx<n and 0<=ny<n):
        if(visited[nx][ny] == -1):
          if(data[nx][ny] == 0):
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))
          elif(data[nx][ny] == 2):
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))

  max_value = check()
  if(max_value != -1):
    result.append(max_value)


  
  
n, m = map(int, input().strip().split())
data = []
com = []
result = []
for i in range(n):
  row = list(map(int, input().strip().split()))

  data.append(row)
  for j in range(len(row)):
    if(data[i][j] == 2):
      com.append((i, j))

com = combinations(com, m)
queue = deque()

for viruses in com:
  visited = [[-1] * n for _ in range(n)]

  for x, y in viruses:
    visited[x][y] = 0
    queue.append((x, y))

  bfs()

if(len(result) == 0):
  print(-1)
else:
  print(min(result))