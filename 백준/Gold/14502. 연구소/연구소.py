from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def create_wall(count):
  global result
  
  if(count == 3):
    for i in range(n):
      for j in range(m):
        temp[i][j] = graph[i][j]
        
    for i in range(n):
        for j in range(m):
          
          if(temp[i][j] == 2):
            bfs(i,j)
    
    score = 0
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 0:
          score += 1
    result = max(result, score)
    return

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        count += 1
        create_wall(count)
        graph[i][j] = 0
        count -= 1


def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while(queue):
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if(0<=nx<n and 0<=ny<m):
        if(temp[nx][ny] == 0):
          queue.append((nx,ny))
          temp[nx][ny] = 2

result = 0
n,m = map(int, input().strip().split())

graph = []
temp = [[0]*m for _ in range(n)]    

for i in range(n):
  graph.append(list(map(int, input().strip().split())))

temp2 = list()
create_wall(0)
print(result)