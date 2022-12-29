import sys 
input = sys.stdin.readline 

n = int(input())
data = list(map(int, input().split()))
data.sort()
left = 0
right = n-1
result = []
min_value = 1e9 * 2

while left<right:
  tot = data[left]+data[right]
  if abs(tot) <= abs(min_value):
    al = left
    ar = right
    min_value = tot

  if tot<0:
    left += 1
  else:
    right -= 1

print(data[al],data[ar])