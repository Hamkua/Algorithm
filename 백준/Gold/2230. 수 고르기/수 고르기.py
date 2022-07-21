import sys

input = sys.stdin.readline
n, m = map(int, input().strip().split())
a = []
for _ in range(n):
  a.append(int(input()))

a.sort()
left = 0
right = 1

result = sys.maxsize

while(left < n and right < n):
  diff = a[right] - a[left]
  if(diff == m):
    result = m
    break 
  elif(diff > m):
    result = min(result, diff)
    left += 1
  else:
    
    right += 1

print(result)