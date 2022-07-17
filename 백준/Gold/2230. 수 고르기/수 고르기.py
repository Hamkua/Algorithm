import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data =[]
left = 0
right = 1

for _ in range(n):
  data.append(int(input()))
data.sort()

min_value = 2 * 1e9

while left<n and right<n:
  result = data[right] - data[left]
  if result == m:
    min_value = m 
    break
  elif result < m:
    right += 1
  else:
    if result <= min_value:
      min_value = result
    left += 1

print(min_value)