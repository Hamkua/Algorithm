import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
data.sort()

left = 0
right = n-1
min_value = 1e9 * 2

while left<right:
  total = data[left]+ data[right]

  if abs(total) <= abs(min_value):
    min_value = total
    l = left
    r = right

  if total < 0:
    left += 1
  if total >= 0:
    right -= 1

print(data[l],data[r])
