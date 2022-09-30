import sys

input = sys.stdin.readline

def backtracking(start):
  if len(visited) == m:
    print(" ".join(map(str, visited)))

  else:
    for i in data:
      if i not in visited:
        visited.append(i)
        backtracking(i)
        visited.pop()


n, m = map(int, input().strip().split())
data = sorted(list(map(int, input().strip().split())))
visited = list()
backtracking(1)