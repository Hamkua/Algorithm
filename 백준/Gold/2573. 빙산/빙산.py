from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs():

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m:
        if visited[nx][ny] == 0 and data[nx][ny] == 0:
          data[x][y] -= 1
          if data[x][y] <= 0:
            data[x][y] = 0

def check(x,y):
  queue.append((x,y))
  visited[x][y] = 2
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m:
        if visited[nx][ny] == 1:
          visited[nx][ny] = 2
          queue.append((nx,ny))
  

n,m = map(int, input().split())
data = []
r = True
t = 0
for _ in range(n):
  data.append(list(map(int,input().split())))


queue = deque()

while r:
  cnt = 0
  visited =[[0]*m for _ in range(n)]
  r = False
  for i in range(n):
    for j in range(m):
      if data[i][j] != 0:
        visited[i][j] = 1
        r = True

  for i in range(n):
    for j in range(m):
      if visited[i][j] == 1:
        check(i,j)
        cnt += 1
  
  if cnt >= 2:
    print(t)
    break
  else:
    for i in range(n):
      for j in range(m):
        if data[i][j] != 0:
          queue.append((i,j))    
  t+= 1
  bfs()      

if r == False:
  print(0)
