import sys
T=int(sys.stdin.readline().rstrip())
for i in range(T):
    A,B=map(int,sys.stdin.readline().split())
    C=A+B
    print("Case #{0}: {1} + {2} = {3}".format(i+1,A,B,C))
