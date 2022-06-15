import sys 
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
data_s = sorted(list(set(data)))
dic = {data_s[i] : i for i in range(len(data_s))}

for i in data:
  print(dic[i],end=" ")
