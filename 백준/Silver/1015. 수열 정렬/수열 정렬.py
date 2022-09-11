import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().strip().split()))

sorted_data = sorted(data.copy())

dictionary = dict()
for i in range(n):
  if sorted_data[i] not in dictionary:
    queue = deque()
    queue.append(i)
    dictionary[sorted_data[i]] = queue
    
  else:
    dictionary[sorted_data[i]].append(i)

for i in data:
  
  temp = dictionary[i].popleft()
  print(temp, end = " ")