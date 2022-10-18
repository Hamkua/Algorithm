from collections import deque
import sys


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(color,x,y):
  queue = deque()
  queue.append((x,y))
  if color == 'B' or color == 'N' :
    graph[x][y] = 'M'
  else:
    graph[x][y] = 'N'

  while(queue):
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if (nx < 0) or (ny < 0) or (nx >= n) or (ny >= n):
        continue
      if graph[nx][ny] != color:
        continue
      if color == 'B' or color == 'N' :
        if graph[nx][ny] == color:
          graph[nx][ny] = 'M'
          queue.append((nx,ny))
      elif color != 'B':
        if graph[nx][ny] == color:
          graph[nx][ny] = 'N'
          queue.append((nx,ny))
  return 0

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(input()))

result = 0
d_result = 0
for i in range(n):
  for j in range(n):
    if graph[i][j] == 'R':
      bfs('R',i,j)
      result += 1
    if graph[i][j] == 'G':
      bfs('G',i,j)
      result += 1
    if graph[i][j] == 'B':
      bfs('B',i,j)
      result += 1 
      d_result += 1
for i in range(n):
  for j in range(n):
    if graph[i][j] == 'N':
      bfs('N',i,j)
      d_result +=1

print(result,d_result,end=" ")