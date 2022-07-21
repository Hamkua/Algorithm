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

# while(left < right):
#   if(a[right] - a[left] == m):
#     result = m
#     break 
#   elif(a[right] - a[left] > m):
    
#     result = min(result, a[right] - a[left])
#     left += 1
#   else:
#     if(right + 1 < len(a)):   <- 이 조건문에도 해당되지 않는 경우 무한루프
#       right += 1

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
