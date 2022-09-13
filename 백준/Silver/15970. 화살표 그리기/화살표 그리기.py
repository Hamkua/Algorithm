import sys

input = sys.stdin.readline
dictionary = dict()
result = 0

n = int(input())

for _ in range(n):
  point, color = map(int, input().strip().split())
  if color not in dictionary:
    dictionary[color] = [point]
  else:
    dictionary[color].append(point)


for key in dictionary.keys():
  dictionary[key].sort()
  # print(dictionary[key])
  for i in range(len(dictionary[key])):
    min_distance = sys.maxsize

    for j in range(len(dictionary[key])):
      # print("i = {}, j = {}".format(i, j))
      if(i == j):
        continue
       
      if min_distance >= abs(dictionary[key][i] - dictionary[key][j]):
        
        min_distance = abs(dictionary[key][i] - dictionary[key][j])
        min_i, min_j = i, j

    result += min_distance
    
print(result)