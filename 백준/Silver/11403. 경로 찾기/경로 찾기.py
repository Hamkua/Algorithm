from collections import deque
import sys
input = sys.stdin.readline

def dijkstra(start):
  visited = [[0]*n for _ in range(n)]
  tmp = [0]*n
  queue = deque()
  queue.append(start)

  while(queue):
    p = queue.popleft()
    for i in data[p]:
      if(visited[p][i] == 0):
        tmp[i] = 1
        queue.append(i)
        visited[p][i] = 1

  return tmp

n = int(input())
data = [[] for _ in range(n)]

for i in range(n):
  row = list(map(int, input().strip().split()))
  for j in range(n):
    if(row[j] == 1):
      data[i].append(j)

result = []

for i in range(n):
  for j in dijkstra(i):
    print(j, end=" ")
  print()