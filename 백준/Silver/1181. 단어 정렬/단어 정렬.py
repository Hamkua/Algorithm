import sys
input = sys.stdin.readline 

n = int(input())
data =[]
s = []
for i in range(n):
  word = input().rstrip()
  if word not in data:
    data.append(word)

data.sort(key = lambda x : (len(x),x))

for i in data:
  print(i)