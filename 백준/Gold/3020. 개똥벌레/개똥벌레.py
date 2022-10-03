import sys
input = sys.stdin.readline 

def binary_search(target, data_list):

  left = 0
  right = len(data_list) - 1
  
  while(left <= right):
    mid = (left + right) // 2 

    if data_list[mid] > target:
      right = mid - 1
    else:
      left = mid + 1
    # print("target = {}, data_list = {}, mid = {}, left = {}, right = {}".format(target, data_list, mid, left, right))

  return len(data_list) - (right + 1)

n, h = map(int, input().strip().split())
data = []
rev_data = []
result_dict = dict()

for i in range(n):
  if i % 2 == 0:
    data.append(int(input()))
  else:
    rev_data.append(int(input()))

data.sort()
rev_data.sort()

result = dict()
for height in range(h):
  a = binary_search(height, data)
  b = binary_search(h - (height + 1), rev_data)
  
  if a+b in result:
    result[a+b] += 1
  else:
    result[a+b] = 1
    

# print(result)
min_key = min(result.keys())
print(min_key, result[min_key])