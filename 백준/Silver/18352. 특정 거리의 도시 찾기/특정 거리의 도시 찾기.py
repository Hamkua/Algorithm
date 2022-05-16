from collections import deque
import sys
input = sys.stdin.readline

#도시 갯수, 도로 갯수, 찾고자하는 최단거리, 출발 도시번호
n,m,k,x = map(int,input().strip().split())    

data = [[] for _ in range(n+1)] 

def bfs(x):

  visited = [-1] * (n+1)
  visited[x] = 0
  queue = deque()
  queue.append(x)

  while(queue):
    x = queue.popleft()
    
    for i in data[x]:
      if(visited[i] == -1):
        visited[i] = visited[x] + 1
        if visited[i] == k:
          result.append(i)
        queue.append(i)
             
result = []

for _ in range(m):
  a,b = map(int, input().strip().split()) 
  data[a].append(b)
    
bfs(x)

if result:
  result.sort()
  for i in result:
    print(i)
    
else:
  print(-1)
