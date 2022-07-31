import sys
input = sys.stdin.readline   

n = int(input())
data = list(map(int,input().split()))

m = int(input())
min_value, max_value = 0,max(data)

while min_value<=max_value:
  mid = (min_value + max_value)//2
  result = 0
  for i in data:
    if i < mid :
      result += i
    else:
      result += mid
  if result <= m:
    min_value = mid + 1
  else:
    max_value = mid - 1
print(max_value)