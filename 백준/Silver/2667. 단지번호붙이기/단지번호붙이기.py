from collections import deque 
import sys

input = sys.stdin.readline

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def bfs(x,y):
  cnt = 1
  queue = deque() 
  queue.append((x,y))
  visited[x][y] = True

  while(queue):
    x, y = queue.popleft() 
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(0<=nx<n and 0<=ny<n):
        if(visited[nx][ny] == False and data[nx][ny] == 1):
          visited[nx][ny] = True
          queue.append((nx,ny))
          cnt += 1

  return cnt

n = int(input())
data = []
visited = [[False]*(n + 1) for _ in range(n + 1)]
result = []

for _ in range(n):
  data.append(list(map(int, input().strip())))

for i in range(n):
  for j in range(n):
    if visited[i][j] == False and data[i][j] == 1:
      result.append(bfs(i,j))

result.sort()
length = len(result)

print(length)

for i in range(length):
  print(result[i])