import sys

input = sys.stdin.readline

n, c = map(int, input().strip().split())

data = list()

for i in range(n):
  data.append(int(input()))
data.sort()

left, right = 1, data[-1] - data[0]

while(left <= right):
  mid = (left + right)//2

  current = data[0]
  cnt = 1

  for i in range(1, len(data)):
    if data[i] - current >= mid:
      current = data[i]
      cnt += 1

  if cnt >= c:
    left = mid + 1

  elif cnt < c:
    right = mid - 1
    
print(right)