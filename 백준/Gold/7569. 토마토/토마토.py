from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,0,0,-1,1]
dy = [-1,1,0,0,0,0]
dz = [0,0,-1,1,0,0]

def bfs():
  # queue = deque()
  # queue.append((x,y,z))

  while(queue):
    x,y,z = queue.popleft()
    tmp = graph[x][y][z] + 1
    
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if(0<=nx<h and 0<=ny<n and 0<=nz<m):
        if(graph[nx][ny][nz] == 0 or graph[nx][ny][nz]>tmp):
          graph[nx][ny][nz] = tmp
          queue.append((nx,ny,nz))
          
m,n,h = map(int, input().strip().split())

graph = [[] for _ in range(h)]

for i in range(h):
  for j in range(n):
    graph[i].append(list(map(int, input().strip().split())))

queue = deque()

for i in range(h):
  for j in range(n):
    for k in range(m):
      if(graph[i][j][k] == 1):
        queue.append((i,j,k))

bfs()

is_ripe = True
max_val = -1
# for i in range(h):
#   for j in range(n):
#     for k in range(m):
#       if(max_val<graph[i][j][k]):
#         max_val = graph[i][j][k]
        
#       if(graph[i][j][k] == 0):
#         is_ripe = False

# if(not is_ripe or max_val<2):
#   print(-1)
# else:
#   print(max_val - 1)
cnt = 0

for i in range(h):
  for j in range(n):
    for z in range(m):
      cnt = max(graph[i][j][z],cnt)
      if graph[i][j][z] == 0:
        print(-1)
        exit()
print(cnt-1)
