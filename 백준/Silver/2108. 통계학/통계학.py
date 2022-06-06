import sys 
from collections import Counter

input = sys.stdin.readline 
n= int(input())

d = []
for i in range(n):
  a = int(input())
  d.append(a)

d.sort()

mean = round(sum(d)/n)
print(mean)

print(d[n//2])

r = max(d) - min(d)

d=Counter(d).most_common()

if len(d)>1:
  
  if d[0][1] == d[1][1]:
      print(d[1][0])
  else:
      print(d[0][0])
else:
    print(d[0][0])

print(r)
