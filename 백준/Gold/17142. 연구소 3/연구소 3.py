import sys
from collections import deque 
from itertools import combinations
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def is_continue(visited):
  for i in range(n):
    for j in range(n):
      if visited[i][j] == -1:
        return False
  return True

def bfs(arr):
  queue = deque()
  visited = [[-1]*n for _ in range(n)]
  for x,y in arr:
    visited[x][y] = 0
    queue.append((x,y))

  for i in range(n):
    for j in range(n):
      if data[i][j] == 1:
        visited[i][j] = -3

  result = 0
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<n:
        if data[nx][ny] == 2 and visited[nx][ny] == -1:
          visited[nx][ny] = visited[x][y]+1
          queue.append((nx,ny))
          
        if data[nx][ny] == 0 and visited[nx][ny] == -1:
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx,ny))
          result = max(result,visited[nx][ny])

  is_con = is_continue(visited)
  if(is_con == False):
    return -1
  return result

n,m = map(int,input().split())
data = []
com = []
answer = []
for _ in range(n):
  data.append(list(map(int,input().split())))

for i in range(n):
  for j in range(n):
    if data[i][j] == 2:
      com.append((i,j))

com = list(combinations(com,m))

for c in com:
  r = bfs(c)
  if r == -1:
    continue
  answer.append(r)

if len(answer) == 0:
  print(-1)
else:
  print(min(answer))