import sys
from collections import deque 

input = sys.stdin.readline 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  cnt = 1
  queue = deque()
  visited[x][y] = True 
  queue.append((x,y))
  while(queue):
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(0<=nx<n and 0<=ny<m):
        if(data[nx][ny] == 1 and visited[nx][ny] == False):
          visited[nx][ny] = True
          cnt += 1
          queue.append((nx,ny))

  return cnt
          

n,m,k = map(int, input().strip().split())
count = 0
data = [[0]*(m+1) for _ in range(n+1)]
visited = [[False]*(m+1) for _ in range(n+1)]

for _ in range(k):
  x,y = map(int, input().strip().split())
  data[x-1][y-1] = 1

for i in range(n):
  for j in range(m):
    if(data[i][j] == 1 and visited[i][j] == False):
      count = max(count, bfs(i,j))

print(count)
  