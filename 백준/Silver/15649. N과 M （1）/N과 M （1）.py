import sys

input = sys.stdin.readline

def backtracking(start):
  if len(visited) == m:
    print(" ".join(map(str, visited)))

  else:
    for i in range(1, n + 1):
      if i not in visited:
        visited.append(i)
        backtracking(i)
        visited.pop()


n, m = map(int, input().strip().split())
# data = [n for n in range(1, n + 1)]
visited = list()
backtracking(1)
