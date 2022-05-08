from collections import deque 

def dfs(x):
  visited[x]=True
  print(x,end=" ")
  for i in graph[x]:
    if visited[i]==False:
      dfs(i)

def bfs(x):
  queue = deque()
  visited[x]=False
  print(x,end=" ")
  for g in graph[x]:
      queue.append(g)
  while(queue):
    q = queue.popleft()
    if visited[q] == True:
      visited[q] = False
      print(q,end=" ")
      for g in graph[q]:
        queue.append(g)

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[a].sort()
  graph[b].append(a)
  graph[b].sort()
  
visited = [False]*(n+1)
dfs(v)
print()
bfs(v)
