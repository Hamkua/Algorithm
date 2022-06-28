import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
  queue = deque()
  queue.append((0, 0))
  visited[0][0] = 0

  while(queue):
    x, y = queue.popleft()
    if(x == n -1 and y == n - 1):
      return visited[n-1][n-1]
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if(0<=nx<n and 0<=ny<n):
        if(data[nx][ny] == 0 and visited[nx][ny] == -1):
          queue.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1
          
        elif(data[nx][ny] == 1 and visited[nx][ny] == -1):
          queue.appendleft((nx, ny))
          visited[nx][ny] = visited[x][y]

result = 0

n = int(input())
data = []
for _ in range(n):
  data.append(list(map(int, input().strip())))

visited = [[-1] * (n + 1) for _ in range(n + 1)]

# for i in range(n):
#   print(data[i])
print(bfs(0,0))