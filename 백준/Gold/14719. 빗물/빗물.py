import sys
input = sys.stdin.readline

h, w = map(int, input().strip().split())
data = list(map(int, input().strip().split()))

volume = 0
left, right = 0, len(data) -1
left_max, right_max = data[left], data[right]

while left < right:
  left_max, right_max = max(left_max, data[left]), max(right_max, data[right])

  if(left_max <= right_max):
    volume += left_max - data[left]
    left += 1

  else:
    volume += right_max - data[right]
    right -= 1

print(volume)