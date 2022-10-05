import sys
input = sys.stdin.readline 


def backtracking(num):
  if len(visited) == m:
    print(" ".join(map(str, visited)))

  else:
    for i in range(1, n + 1):
      
      visited.append(i)
      backtracking(i)
      visited.pop()
    
visited = []
n, m = map(int, input().strip().split())
backtracking(1)