import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().strip().split())
graph = [[] for _ in range(n+1)]
result = []
max_cnt = -1

def bfs(x):
  global max_cnt
  cnt = 0
  visited = [False]*(n+1)
  visited[x] = True
  queue = deque()
  queue.append(x)

  while(queue):
    x = queue.popleft()
    cnt+=1
    for i in graph[x]:
      if visited[i] == False:
        visited[i] = True
        queue.append(i)
        # cnt += 1

  return cnt

for _ in range(m):
  a,b= map(int,input().strip().split())
  if(a not in graph[b]):
    graph[b].append(a)

for i in range(1,n+1):
  if graph[i]:
    tmp = bfs(i)
    if tmp>=max_cnt:
      if(tmp>max_cnt):
        result = []
      max_cnt = tmp
      result.append(i)

for i in result:
  if(i):
    print(i, end=" ")

