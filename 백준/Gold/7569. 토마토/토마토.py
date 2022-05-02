from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
  while queue:
    x,y,z = queue.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if nx<0 or ny<0 or nz<0 or nx>=h or ny>=n or nz>=m:
        continue
      if data[nx][ny][nz] == 0:
        data[nx][ny][nz] = data[x][y][z] + 1
        queue.append((nx,ny,nz))

cnt = 0
isT = False
m,n,h = map(int,input().split())    #가로, 세로, 높이
data = [[] for _ in range(h)]

for i in range(h):
  for j in range(n):
    data[i].append(list(map(int,input().split())))

queue = deque()

for i in range(h):
  for j in range(n):
    for z in range(m):
      if data[i][j][z] == 1:
        queue.append((i,j,z))

bfs()

for i in range(h):
  for j in range(n):
    for z in range(m):
      cnt = max(data[i][j][z],cnt)
      if data[i][j][z] == 0:
        print(-1)
        exit()
print(cnt-1)