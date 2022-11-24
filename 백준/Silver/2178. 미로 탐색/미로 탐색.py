import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  queue= deque()
  queue.append((x,y))
  while queue:
    a,b = queue.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if nx<0 or ny <0 or nx>=n or ny>=m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[a][b] + 1 
        queue.append((nx,ny))
  return graph[n-1][m-1]

n,m = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().strip())))
print(bfs(0,0))