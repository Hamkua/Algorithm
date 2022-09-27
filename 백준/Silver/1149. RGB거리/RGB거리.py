import sys
input = sys.stdin.readline

n = int(input())
result = list()

for _ in range(n):
  r, g, b = map(int, input().strip().split())
  
  if len(result) == 0:
    result.append(r)
    result.append(g)
    result.append(b)
  else:
    tmp = result.copy()
    result[0] = min(r + tmp[1], r + tmp[2])
    result[1] = min(g + tmp[0], g + tmp[2])
    result[2] = min(b + tmp[0], b + tmp[1])

print(min(result))