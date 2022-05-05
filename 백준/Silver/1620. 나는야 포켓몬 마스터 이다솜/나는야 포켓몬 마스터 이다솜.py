import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())

dic = dict()
answer = list()
for i in range(n):
  dic[i+1] = input().strip()

reversed_dict = {value:key for key, value in dic.items()}

for _ in range(m):
  q = input().strip()
  
  if(str.isdigit(q)):
    answer.append(dic[int(q)])
    
  else:
    answer.append(reversed_dict[q])
        
for a in answer:
  print(a)