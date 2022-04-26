from collections import deque

def bfs():
  queue = deque()
  queue.append(1)

  while queue:
    q = queue.popleft()
    for g in graph[q]:
      if visited[g] == False:
        visited[g] = True
        queue.append(g)

  return sum(visited)-1


n = int(input())
m = int(input())
result = 0
visited = [False]*(n+1)
graph=[[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

print(bfs())