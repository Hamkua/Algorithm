import sys
N=int(sys.stdin.readline().rstrip())
a=[]
for _ in range(N):
    weight,height=map(int,sys.stdin.readline().split())
    a.append((weight,height))
for i in a:
    rank=1
    for j in a:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank,end=" ")