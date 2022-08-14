import sys
input = sys.stdin.readline

alist = []
blist = []
clist = []
dlist = []

n = int(input())
for i in range(n):
  a,b,c,d = map(int,input().split())
  alist.append(a), blist.append(b), clist.append(c), dlist.append(d)
cnt = 0
dic = dict()
for a in alist:
  for b in blist:
    dic[a+b] = dic.get(a+b,0)+1

for c in clist:
  for d in dlist:
    cnt += dic.get(-(c+d),0)
print(cnt)