import sys
input = sys.stdin.readline 

n = int(input())
data = dict()
for _ in range(n):
  m = int(input())
  if m in data.keys():
    data[m] += 1
  else:
    data[m] = 1

data = sorted(data.items(), key = lambda x: (-x[1],x[0]))
print(data[0][0])