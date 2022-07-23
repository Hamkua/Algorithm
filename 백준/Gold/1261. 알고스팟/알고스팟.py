from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
  visited = [[-1]*(n) for _ in range(m)]

  queue = deque()
  queue.append((0,0))
  visited[0][0] = 0

  while(queue):
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if(0<=nx<m and 0<=ny<n):

        if(visited[nx][ny] == -1):
          if(data[nx][ny] == 0):
            queue.appendleft((nx,ny))
            visited[nx][ny] = visited[x][y]

          elif(data[nx][ny] == 1):
            queue.append((nx,ny))
            visited[nx][ny] = visited[x][y] + 1


  return visited[m-1][n-1]
            
n, m = map(int, input().strip().split())

data = []
for _ in range(m):
  data.append(list(map(int, input().strip())))

print(bfs())