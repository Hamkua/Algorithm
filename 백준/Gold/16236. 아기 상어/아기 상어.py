from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

shark = 2
size = 0
t = 0

def bfs(x,y,t):
  global shark, size
  visited = [[-1]*n for _ in range(n)]    #거리와 방문여부를 확인할 목적의 리스트
  visited[x][y] = t
  queue = deque()
  queue.append((x,y))
  can_eat = []

  while queue:
    qlen = len(queue)
    
    while qlen:
      x, y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
          if visited[nx][ny] == -1:
              if graph[nx][ny] == 0 or graph[nx][ny] == shark:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

              if (0 < graph[nx][ny] < shark) :               
                can_eat.append([nx,ny])
      qlen -= 1

    if can_eat:
      xx,yy = min(can_eat)
      size += 1
      if shark == size:
          shark += 1
          size = 0
      graph[xx][yy] = 0 
      return xx,yy,visited[x][y]+1
  print(t)
  sys.exit()

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            s_x, s_y = i , j
            graph[i][j] = 0

while True:
    s_x,s_y,t = bfs(s_x,s_y,t)