import sys 
from collections import Counter

input = sys.stdin.readline 

n = int(input())
data = Counter(list(map(int, input().split())))
m = int(input())
data_2 = list(map(int, input().split()))

r = [0]*len(data_2)

for i in range(m):
  try:
    r[i] = data[data_2[i]]
  except:
    r[i] = 0

for i in r:
  print(i,end= " ")

  