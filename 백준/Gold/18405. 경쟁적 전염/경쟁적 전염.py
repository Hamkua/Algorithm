from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,k = map(int,input().split())

graph = []
data = []
for i in range(n):
  graph.append(list(map(int,input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      data.append((graph[i][j],0,i,j))

data.sort()
q = deque(data)

s,target_x,target_y = map(int,input().split())    #초, 좌표 

while q:
  virus,sec,x,y = q.popleft()
  if sec == s:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx<0 or ny<0 or nx>=n or ny>=n:
      continue
    if graph[nx][ny] == 0:
      graph[nx][ny] = virus
      q.append((virus,sec+1,nx,ny))

print(graph[target_x-1][target_y-1])