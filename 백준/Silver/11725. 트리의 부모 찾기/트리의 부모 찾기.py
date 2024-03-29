from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  queue = deque()
  queue.append(1)
  visited[1]= 1
  while queue:
    q = queue.popleft()
    for i in graph[q]:

      if visited[i] == -1:
        visited[i] = q
        queue.append(i)

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [-1]*(n+1)

for _ in range(n-1):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

bfs()

for i in range(2,n+1):
  print(visited[i])