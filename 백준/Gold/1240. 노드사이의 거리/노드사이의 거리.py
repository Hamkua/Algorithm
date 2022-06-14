from collections import deque
import sys
input = sys.stdin.readline


def bfs(start, end):
  queue = deque()
  
  for i in range(len(data[start])):
    queue.append(data[start][i])

  while(queue):
    pop_list = queue.popleft()

    starting_point = pop_list[0]
    destination = pop_list[1]
    distance = pop_list[2]

    if(starting_point == end):
      # print(" ------ ")
      # for i in range(n + 1):
      #   print(visited[i])
      return visited[end]

    if(visited[destination] == 0 or visited[destination] > visited[starting_point] + distance):
      visited[destination] = visited[starting_point] + distance
      for i in range(len(data[destination])):
        queue.append(data[destination][i])
        
    
n, m = map(int, input().strip().split())
data = [[] for _ in range(n+1)]

for _ in range(1, n):
  a_node, b_node, edge = map(int, input().strip().split())
  data[a_node].append([a_node, b_node, edge])
  data[b_node].append([b_node, a_node, edge])

# for i in range(n + 1):
#   print(data[i])

for _ in range(m):
  start_node, end_node = map(int, input().strip().split())
  visited = [0 for _ in range(n+1)]
  print(bfs(start_node, end_node))