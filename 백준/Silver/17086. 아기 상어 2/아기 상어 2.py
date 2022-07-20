from collections import deque
import sys

input = sys.stdin.readline


dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,1,-1,-1,1]

n, m = map(int, input().strip().split())
data = []
result = [[-1] * m for _ in range(n)]

for _ in range(n):
  data.append(list(map(int, input().strip().split())))

for a in range(n):
  for b in range(m):
    queue = deque()

    if data[a][b] == 0:
      visited = [[-1] * m for _ in range(n)]
    
      queue.append((a,b))  
      visited[a][b] = 0

      while(queue):
        x, y = queue.popleft()
        if data[x][y] == 1:
          result[x][y] = max(result[x][y], visited[x][y])
          break
          
        for i in range(8):
          nx = x + dx[i];
          ny = y + dy[i];

          if(0<=nx<n and 0<=ny<m):
            if(visited[nx][ny] == -1):
              queue.append((nx, ny))
              visited[nx][ny] = visited[x][y] + 1
          
print(max(map(max, result)))



# from collections import deque
# import sys 
# input = sys.stdin.readline

# queue = deque()

# dx = [-1,1,0,0,-1,-1,1,1]
# dy = [0,0,-1,1,-1,1,-1,1]

# def bfs():
#   r = 0

#   while queue:
#     x, y = queue.popleft()
#     for i in range(8):
#       nx = x + dx[i]
#       ny = y + dy[i]

#       if 0>nx or 0>ny or nx>=n or ny>=m:
#         continue

#       if graph[nx][ny] == 0:
#         graph[nx][ny] = graph[x][y] + 1
#         queue.append((nx,ny))
#         r = max(r, graph[nx][ny])
#   return r-1
        
#       # elif graph[x][y] + 1 <= graph[nx][ny]:
#       #   graph[nx][ny] = graph[x][y] + 1
#       #   queue.append((nx,ny))

# n,m = map(int,input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(int,input().split())))

# result = 0
# for i in range(n):
#   for j in range(m):
#     if graph[i][j] == 1:
#       queue.append((i,j))
      
# bfs()

# for i in range(n):
#   for j in range(m):
#     result = max(result, graph[i][j])
# print(result -1)
