import sys
input = sys.stdin.readline  

n = int(input())
dic = dict()
result = []
for _ in range(n):
  a = input().rstrip()
  if a not in dic:
    dic[a] = 1
  else:
    dic[a] += 1

max_value = max(dic.values())

for i,j in dic.items():
  if j == max_value:
    result.append(i)

result.sort()
print(result[0])
